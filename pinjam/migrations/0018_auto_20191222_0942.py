# Generated by Django 3.0.1 on 2019-12-22 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0017_auto_20191221_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
        migrations.AlterField(
            model_name='senjata',
            name='id_detail_senjata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.DetailSenjata'),
        ),
    ]
