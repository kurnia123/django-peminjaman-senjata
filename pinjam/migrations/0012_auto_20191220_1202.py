# Generated by Django 3.0.1 on 2019-12-20 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0011_auto_20191220_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailsenjata',
            name='nama_senjata',
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]
