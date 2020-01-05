from django.urls import path,re_path as url

from .views import (lengkapi_data_pribadi_karyawan,
	singup_view,
	loginView,
	kode_booking,
	PilihMenu,
	kode_pengembalian)

app_name="karyawan"
urlpatterns = [
	url(r'^$',singup_view,name="karyawan_signup"),
	url(r'^complited/(?P<namakaryawan>[\w]+)',lengkapi_data_pribadi_karyawan,name='complited_karyawan'),
	url(r'^login/',loginView,name='login_karyawan'),
	url(r'^kd-booking/',kode_booking,name='kdbooking'),
	url(r'^kd-pengembalian',kode_pengembalian,name='kdpengembalian'),
	url(r'^pilihmenu/',PilihMenu.as_view(),name='pilihmenu'),
]