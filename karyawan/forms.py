from django import forms

from .models import Karyawan
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=50,required=False)
	password1 = forms.CharField(widget=forms.PasswordInput(),help_text='Gunakan Huruf besar [a-A],character',required=False)
	password2 = forms.CharField(widget=forms.PasswordInput(),help_text='Confirm Password',required=False)

	class Meta:
		model = User
		fields = ('username','password1', 'password2')



class KaryawanPostForm(forms.ModelForm):
	class Meta:
		model = Karyawan
		fields = [
			'id_karyawan',
			'nama_karyawan',
			'jenis_kelamin_karyawan',
			'alamat_karyawan',
			'no_ktp_karyawan',
		]
