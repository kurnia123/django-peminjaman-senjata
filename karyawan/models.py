from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Karyawan(models.Model):
    JENIS_KELAMIN = (
        ('L','Laki-Laki'),
        ('P','Perempuan'),
        )

    id_karyawan = models.CharField(primary_key=True, max_length=10)
    nama_karyawan = models.CharField(max_length=30)
    jenis_kelamin_karyawan = models.CharField(choices=JENIS_KELAMIN,max_length=10,default='L')
    alamat_karyawan = models.CharField(max_length=50)
    no_ktp_karyawan = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def save(self):
        usr = User.objects.get(username=self.nama_karyawan)
        self.user = usr
        super(Karyawan,self).save()

    def __str__(self):
        return "{}.{}".format(self.id_karyawan,self.nama_karyawan)
   
   

