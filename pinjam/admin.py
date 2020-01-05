from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Produsen)
admin.site.register(DetailSenjata)
admin.site.register(Senjata)
admin.site.register(Peminjam)
admin.site.register(PeminjamanSenjata)
admin.site.register(Booking)