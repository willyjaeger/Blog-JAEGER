# Generated by Django 4.2.3 on 2023-09-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0002_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
