# Generated by Django 2.1.5 on 2019-01-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_auto_20190105_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='format',
            field=models.CharField(choices=[('MP3', 'MP3'), ('WMA', 'WMA'), ('WAV', 'WAV')], max_length=4, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='format',
            field=models.CharField(choices=[('JPG', 'JPG'), ('GIF', 'GIF'), ('PNG', 'PNG')], max_length=3, verbose_name='Format'),
        ),
    ]