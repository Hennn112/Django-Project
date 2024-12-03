# Generated by Django 5.1.3 on 2024-11-30 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-tahun_rilis'], 'verbose_name': 'Film', 'verbose_name_plural': 'Film-Film'},
        ),
        migrations.RemoveField(
            model_name='film',
            name='tanggal_rilis',
        ),
        migrations.AddField(
            model_name='film',
            name='tahun_rilis',
            field=models.IntegerField(default=1, verbose_name='Tahun Rilis'),
            preserve_default=False,
        ),
    ]