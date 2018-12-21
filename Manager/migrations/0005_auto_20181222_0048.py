# Generated by Django 2.0.7 on 2018-12-21 23:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_folder_unique'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'ordering': ['date'], 'verbose_name_plural': 'Audios'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['date'], 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ['name'], 'verbose_name_plural': 'Folders'},
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['date'], 'verbose_name_plural': 'Pictures'},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['date'], 'verbose_name_plural': 'Videos'},
        ),
        migrations.AlterField(
            model_name='folder',
            name='unique',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='hash'),
        ),
    ]