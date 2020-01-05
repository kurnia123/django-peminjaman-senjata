from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import PeminjamPostForm,SignUpForm,PeminjamanSenjataForm,BookingForm
from .models import Senjata,DetailSenjata,Peminjam,Booking,PeminjamanSenjata

from django.utils.text import get_valid_filename
import random
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def loginView(request):
	model = User.objects.all()
	context = {
		'page_title':'LOGIN USER',
		'link_singup':'pinjam:signup',
		'user':model,
	}

	user = None
	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request,username=username_login,password=password_login)
		try:
			id_peminjam = user.peminjam.id_peminjaman
			if id_peminjam[0] == "M":
				if user is not None:
					login(request,user)
					return redirect('/pinjam/')
				else:
					return redirect('/pinjam/login/')
			else:
				return redirect('/pinjam/login/')
		except Exception as e:
			redirect('/pinjam/login/')


	return render(request, 'pinjam/login.html',context)


@login_required(login_url='/pinjam/login/')
def logoutView(request):
	logout(request)	
	return redirect("/pinjam/login/")



def singup_view(request):
	form = SignUpForm(request.POST)

	context = {
		'page_title':'Create User',
		'form': form,
	}

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			# set permission
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')

			set_user = User.objects.get(username=username)
			group_permission = Group.objects.get(name='user')
			set_user.groups.add(group_permission)
			set_user.save()

			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/pinjam/complited/{}'.format(username))
		else:
			return redirect('/pinjam/login/')
	return render(request, 'pinjam/signup.html', context)


@login_required(login_url='/pinjam/login/')
def lengkapi_data_pribadi(request,namapeminjam):
	peminjam_form = PeminjamPostForm(request.POST or None)

	value = str(random.randint(1000,9999))
	iddata = "M" + value

	context = {
		'page_title':'Lengkapi Data User',
		'peminjam_form':peminjam_form,
		'nama':namapeminjam,
	}

	try:
		id_data = DetailSenjata.objects.get(id_detail_senjata=iddata)
	except ObjectDoesNotExist:
		print("data tidak ada")
		context['iddata'] = iddata

	if request.method == 'POST':
		if peminjam_form.is_valid():
			peminjam_form.save()
			return redirect('/pinjam/')
	return render(request, 'pinjam/lengkapi_data_pribadi.html', context)



class ListSenjata():
	model = Senjata

	def get_list_senjata_perkategori(self):
		tipeSenjata = self.model.objects.values_list('id_detail_senjata__tipe_senjata',flat=True).distinct()
		
		queryset = []
		context = {}

		for tipe in tipeSenjata :
			tipeNew = self.model.objects.filter(id_detail_senjata__tipe_senjata=tipe)
			gg = get_valid_filename(tipe)
			# queryset.append(tipeNew)
			context[gg] = tipeNew

		return context
		


class ListPinjamSenjata(LoginRequiredMixin,TemplateView,ListSenjata):
	"""docstring for ListPinjamSenjata"""
	template_name = "pinjam/index.html"
	# redirect to Login
	login_url = '/pinjam/login/'

	def get_context_data(self):
		context = self.get_list_senjata_perkategori()
		return context



@login_required(login_url='/pinjam/login/')
def peminjamansenjata(request,idsenjata,idpeminjam):
	pinjamsenjata = PeminjamanSenjataForm(request.POST or None)

	value = str(random.randint(1000,9999))
	iddata = "P" + value

	context = {
		'page_title':'Register',
		'pinjamsenjata':pinjamsenjata,
		'idsenjata':idsenjata,
		'idpeminjam':idpeminjam
	}

	try:
		id_data = DetailSenjata.objects.get(id_detail_senjata=iddata)
	except ObjectDoesNotExist:
		print("data tidak ada")
		context['idpenyewaan'] = iddata

	if request.method == 'POST':
		if pinjamsenjata.is_valid():
			pinjamsenjata.save()
			return redirect('/karyawan/pilihmenu/')
	return render(request, 'pinjam/peminjamansenjata.html', context)



@login_required(login_url='/pinjam/login/')
def actionBooking(request,idsenjata):
	bookingform = BookingForm(request.POST or None)

	value = str(random.randint(1000,9999))
	iddata = "BO" + value

	datasenjata = Senjata.objects.get(id_senjata=idsenjata)
	namaSenjata = datasenjata.nama_senjata

	context = {
		'bookingform':bookingform,
		'idsenjata':idsenjata,
		'namaSenjata':namaSenjata
	}

	if datasenjata.jumlah_tersedia <= 0:
		return redirect('/pinjam/')
	else:
		try:
			Booking.objects.get(id_booking=iddata)
		except Exception as e:
			context['idbooking'] = iddata

		if request.method == 'POST':
			if bookingform.is_valid():
				bookingform.save()
				return redirect('/pinjam/')
			else:
				return redirect('/pinjam/')

	return render(request, 'pinjam/actionbooking.html', context)


@login_required(login_url='/pinjam/login/')
def deleteBooking(request,idbooking,idpenyewa):
	
	try:
		# query mengambil data Booking
		data = Booking.objects.get(id_booking=idbooking)
		# melakukan penambahan jumlah senjata di tabel senjata
		jumlah = data.id_senjata.jumlah_tersedia + 1
		data.id_senjata.jumlah_tersedia = jumlah
		# save query tabel senjata
		data.id_senjata.save()
		# delete data tabel Booking
		data.delete()
	except Exception as e:
		raise e

	return redirect('/pinjam/bookingview/{}/'.format(idpenyewa))



@login_required(login_url='/pinjam/login/')
def BooingViews(request,idpeminjam):
	context = {}

	try:
		get_data = Booking.objects.get(id_penyewa_id=idpeminjam)
		context['data_booking'] = get_data
		context['false'] = "ada"
	except Exception as e:
		context['false'] = 'tidak ada list booking'
	

	return render(request,'pinjam/bookingview.html',context)

 




@login_required(login_url='/pinjam/login/')
def detailSenjataView(request,idsenjata):
	model = Senjata
	data_detail_senjata = model.objects.get(id_senjata=idsenjata)

	context = {
		'list_data_detail':data_detail_senjata
	}

	return render(request,'pinjam/list_data_detail.html',context)