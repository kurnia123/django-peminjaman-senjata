from django.urls import path,re_path as url

from .views import (loginView,
	ListPinjamSenjata,
	logoutView,singup_view,
	lengkapi_data_pribadi,
	peminjamansenjata,
	actionBooking,
	BooingViews,
	deleteBooking,
	detailSenjataView,
	profileView)

app_name="pinjam"
urlpatterns = [
	url(r'^$',ListPinjamSenjata.as_view(),name="list_senjata"),
	url(r'^login/',loginView,name='login'),
	url(r'^logout/',logoutView,name='logout'),
	url(r'^signup/',singup_view,name='signup'),
	url(r'^pinjamsenjata/(?P<idsenjata>[\w]+)/(?P<idpeminjam>[\w]+)',peminjamansenjata,name='pinjamsenjata'),
	url(r'^actionbooking/(?P<idsenjata>[\w]+)',actionBooking,name='actionbooking'),
	url(r'^complited/(?P<namapeminjam>[\w]+)',lengkapi_data_pribadi,name='complited'),
	url(r'^bookingview/(?P<idpeminjam>[\w]+)',BooingViews,name='bookingview'),
	url(r'^deletebooking/(?P<idbooking>[\w]+)/(?P<idpenyewa>[\w]+)/',deleteBooking,name='deletebooking'),
	url(r'^profileView/(?P<idpeminjam>[\w]+)',profileView,name='profileView'),
	url(r'^detailsenjata/(?P<idsenjata>[\w]+)',detailSenjataView,name='detail_senjata')
]