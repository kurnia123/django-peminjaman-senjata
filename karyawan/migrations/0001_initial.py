# Generated by Django 3.0.1 on 2019-12-23 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id_karyawan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_karyawan', models.CharField(max_length=30)),
                ('jenis_kelamin_karyawan', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], default='L', max_length=10)),
                ('alamat_karyawan', models.CharField(max_length=50)),
                ('no_ktp_karyawan', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
