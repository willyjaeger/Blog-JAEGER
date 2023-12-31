# Generated by Django 4.2.3 on 2023-09-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=40)),
                ('nombre', models.CharField(default='', max_length=40)),
                ('apellido', models.CharField(default='', max_length=40)),
                ('contraseña', models.CharField(max_length=40)),
                ('email', models.EmailField(default='', max_length=40, null=True)),
            ],
        ),
    ]
