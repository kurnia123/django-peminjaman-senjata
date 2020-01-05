from django.db import models
from django.contrib.auth.models import User
from karyawan.models import Karyawan

# Create your models here.
class Produsen(models.Model):
	id_produsen = models.CharField(primary_key=True, max_length=10)
	nama_produsen = models.CharField(max_length=30)
	alamat_produsen = models.IntegerField()
     
	def __str__(self):
		return "{}.{}".format(self.id_produsen,self.nama_produsen)


class DetailSenjata(models.Model):
    TIPE_CHOICE = (
        ("Sniper Rifle","Sniper Rifle"),
        ("Machine Gun","Machine Gun"),
        ("Assault Rifle","Assault Rifle"),
        ("Shotgun","Shotgun"),
    )
 	# pk
    id_detail_senjata = models.CharField(primary_key=True, max_length=50)
    tipe_senjata = models.CharField(choices=TIPE_CHOICE,
        max_length=30,default='Shotgun')
    tipe_peluru = models.CharField(max_length=30)
    # fk
    nama_produsen = models.ForeignKey(Produsen, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}.  {}".format(self.id_detail_senjata,self.tipe_senjata)


class Senjata(models.Model):
    id_senjata = models.CharField(primary_key=True, max_length=10)
    nama_senjata = models.CharField(max_length=30)
    jumlah_tersedia = models.IntegerField()
    # fk
    id_detail_senjata = models.OneToOneField(DetailSenjata, on_delete=models.CASCADE,null=True)
    link_image = models.CharField(max_length=50)

    def __str__(self):
        return "{}.{}".format(self.id_senjata,self.nama_senjata)
    

class Peminjam(models.Model):

    JENIS_KELAMIN = (
        ('L','Laki-Laki'),
        ('P','Perempuan'),
        )

    id_peminjaman = models.CharField(primary_key=True, max_length=10)
    nama_peminjam = models.CharField(max_length=30)
    jenis_kelamin_peminjam = models.CharField(choices=JENIS_KELAMIN,max_length=10,default='L')
    alamat_peminjam = models.CharField(max_length=50)
    no_ktp_peminjam = models.CharField(max_length=18)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def save(self):
        usr = User.objects.get(username=self.nama_peminjam)
        self.user = usr
        super(Peminjam,self).save()

    def __str__(self):
        return "{}. {}".format(self.id_peminjaman,self.nama_peminjam)
    

class PeminjamanSenjata(models.Model):
    id_penyewaan = models.CharField(primary_key=True, max_length=50)
    id_peminjaman = models.OneToOneField(Peminjam, on_delete=models.DO_NOTHING,null=True)
    id_senjata = models.ForeignKey(Senjata, on_delete=models.DO_NOTHING,null=True)
    id_karyawan = models.ForeignKey(Karyawan, on_delete=models.DO_NOTHING, null=True)
    tanggal_pinjam = models.DateField()

    def __str__(self):
        return "{}.{}".format(self.id_karyawan,self.tanggal_pinjam)
              

class Booking(models.Model):
    id_booking = models.CharField(primary_key=True, max_length=10)
    id_id_penyewa = models.CharField(max_length=50,null=True)
    id_id_senjata = models.CharField(max_length=50,null=True)
    id_penyewa = models.ForeignKey(Peminjam, on_delete=models.DO_NOTHING,null=True)
    id_senjata = models.ForeignKey(Senjata, on_delete=models.DO_NOTHING,null=True)

    def save(self):
        peminjam = Peminjam.objects.get(id_peminjaman=self.id_id_penyewa)
        senjata = Senjata.objects.get(id_senjata=self.id_id_senjata)

        snjt = senjata.jumlah_tersedia - 1
        senjata.jumlah_tersedia = snjt
        senjata.save()

        self.id_penyewa = peminjam
        self.id_senjata = senjata
        super(Booking,self).save()


    def __str__(self):
        return "{}".format(self.id_booking)