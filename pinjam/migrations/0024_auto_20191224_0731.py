# Generated by Django 3.0.1 on 2019-12-24 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0023_auto_20191224_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id_senjata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pinjam.Senjata'),
        ),
        migrations.AlterField(
            model_name='peminjamansenjata',
            name='id_senjata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pinjam.Senjata'),
        ),
    ]
