# Generated by Django 3.0.1 on 2019-12-19 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0005_auto_20191219_1045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Peminjaman',
            new_name='Peminjam',
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]
