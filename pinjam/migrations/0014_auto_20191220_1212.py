# Generated by Django 3.0.1 on 2019-12-20 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0013_auto_20191220_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsenjata',
            name='tipe_senjata',
            field=models.CharField(choices=[('Sniper Rifle', 'Sniper Rifle'), ('Carbine', 'Carbine'), ('Assault Rifle', 'Assault Rifle'), ('Shotgun', 'Shotgun')], default='Shotgun', max_length=30),
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]
