# Generated by Django 3.0.1 on 2019-12-19 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinjam', '0007_auto_20191219_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peminjamansenjata',
            name='user',
        ),
        migrations.AddField(
            model_name='peminjam',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]
