# Generated by Django 2.1.5 on 2019-01-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_auto_20190106_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='format',
            field=models.CharField(choices=[('DOC', 'DOC'), ('PDF', 'PDF')], max_length=4, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='format',
            field=models.CharField(choices=[('JPG', 'JPG'), ('GIF', 'GIF'), ('PNG', 'PNG')], max_length=4, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='format',
            field=models.CharField(choices=[('MP4', 'MP4'), ('AVI', 'AVI'), ('MOV', 'MOV')], max_length=4, verbose_name='Format'),
        ),
    ]
