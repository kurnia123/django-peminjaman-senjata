from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import KaryawanPostForm,SignUpForm
from .models import Karyawan
from pinjam.models import Booking,PeminjamanSenjata
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import permission_required

import random
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def loginView(request):
	model = User.objects.all()
	context = {
		'page_title':'LOGIN KARYAWAN',
		'link_singup':'karyawan:karyawan_signup',
		'user':model,
	}

	user = None
	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request,username=username_login,password=password_login)
		try:
			id_nama = user.karyawan.id_karyawan
			print(id_nama[0])
			if  id_nama[0] == 'K':
				if user is not None:
					login(request,user)
					return redirect('/karyawan/pilihmenu/')
				else:
					return redirect('/karyawan/login/')
			else:
				return redirect('/karyawan/login/')
		except Exception as e:
			return redirect('/karyawan/login/')

	return render(request, 'pinjam/login.html',context)



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
			set_user.is_staff = True
			set_user.is_superuser = True
			group_permission = Group.objects.get(name='karyawan')
			set_user.groups.add(group_permission)
			set_user.save()

			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/karyawan/complited/{}'.format(username))
		else:
			return redirect('/pinjam/login/')
	return render(request, 'karyawan/signup.html', context)



def lengkapi_data_pribadi_karyawan(request,namakaryawan):
	karyawan_form = KaryawanPostForm(request.POST or None)

	value = str(random.randint(1000,9999))
	iddata = "K" + value

	context = {
		'page_title':'Lengkapi Data User',
		'karyawan_form':karyawan_form,
		'nama':namakaryawan,
	}

	try:
		id_data = Karyawan.objects.get(id_karyawan=iddata)
	except ObjectDoesNotExist:
		print("data tidak ada")
		context['iddata'] = iddata


	if request.method == 'POST':
		if karyawan_form.is_valid():
			karyawan_form.save()
			return redirect('/pinjam/')
	return render(request, 'karyawan/lengkapi_data_pribadi_karyawan.html', context)



@login_required(login_url='/karyawan/login/')
@permission_required('karyawan.add_karyawan')
def kode_booking(request):
	model = Booking

	if request.method == "POST":
		kdbooking = request.POST['kodebooking']
		print(kdbooking)

		try:
			data = model.objects.get(id_booking=kdbooking)
			data.delete()
			print("berhasil")
			# redirect('/karyawan/')
			return redirect('/pinjam/pinjamsenjata/{}/{}/'.format(data.id_senjata_id,data.id_penyewa_id))
		except Exception as e:
			print('data tidak ada')
			redirect('/karyawan/kd-booking/')

	context = {
		'page_title':'Kode Booking',
		'idhtml':'kodebooking'
	}

	return render(request, 'karyawan/kode_booking.html', context)


@login_required(login_url='/karyawan/login/')
@permission_required('karyawan.add_karyawan')
def kode_pengembalian(request):
	model = PeminjamanSenjata

	if request.method == "POST":
		kdbooking = request.POST['kodebooking']
		print(kdbooking)

		try:
			data = model.objects.get(id_penyewaan=kdbooking)

			jumlah = data.id_senjata.jumlah_tersedia + 1
			data.id_senjata.jumlah_tersedia = jumlah
			data.id_senjata.save()

			data.delete()
			print("berhasil")
			# redirect('/karyawan/')
			return redirect('/karyawan/pilihmenu/')
		except Exception as e:
			print('data tidak ada')
			redirect('/karyawan/kd-pengembalian/')

	context = {
		'page_title':'Kode Penyewaan',
		'idhtml':'kodebooking'
	}

	return render(request, 'karyawan/kode_booking.html', context)



class PilihMenu(LoginRequiredMixin,TemplateView):
	"""docstring for PilihMenu"""
	login_url = '/karyawan/login/'
	template_name = 'karyawan/pilihmenu.html'

		