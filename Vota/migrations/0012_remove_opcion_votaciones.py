# Generated by Django 2.0 on 2018-02-14 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vota', '0011_remove_votacion_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcion',
            name='votaciones',
        ),
    ]