# Generated by Django 3.0.1 on 2019-12-19 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0008_auto_20191219_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]