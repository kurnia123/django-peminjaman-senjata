# Generated by Django 3.0.1 on 2019-12-20 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0010_auto_20191219_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailsenjata',
            old_name='ipe_peluru',
            new_name='tipe_peluru',
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pinjam.Senjata'),
        ),
    ]