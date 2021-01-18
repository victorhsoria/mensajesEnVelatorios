# Generated by Django 3.1.2 on 2021-01-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_auto_20200622_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Artículos'},
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Miniatura'),
        ),
    ]
