from django import forms

from .models import Peminjam,PeminjamanSenjata,Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PeminjamPostForm(forms.ModelForm):
	class Meta:
		model = Peminjam
		fields = [
			'id_peminjaman',
			'nama_peminjam',
			'jenis_kelamin_peminjam',
			'alamat_peminjam',
			'no_ktp_peminjam',

		]
	"""docstring for PeminjamPostForm"""


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=50,required=False)
	password1 = forms.CharField(widget=forms.PasswordInput(),help_text='Gunakan Huruf besar [a-A],character',required=False)
	password2 = forms.CharField(widget=forms.PasswordInput(),help_text='Confirm Password',required=False)

	class Meta:
		model = User
		fields = ('username','password1', 'password2')


class PeminjamanSenjataForm(forms.ModelForm):
    class Meta:
        model = PeminjamanSenjata
        fields = [
        'id_penyewaan',
        'id_peminjaman',
        'id_senjata',
        'id_karyawan',
        'tanggal_pinjam'
        ]



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
        	'id_booking',
        	'id_id_penyewa',
        	'id_id_senjata',
        ]