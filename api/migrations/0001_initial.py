# Generated by Django 5.0.4 on 2024-04-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
