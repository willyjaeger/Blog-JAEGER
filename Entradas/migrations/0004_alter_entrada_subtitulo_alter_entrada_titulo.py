# Generated by Django 4.2.3 on 2023-09-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0003_alter_entrada_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='subtitulo',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=160),
        ),
    ]