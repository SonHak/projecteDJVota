# Generated by Django 2.0 on 2018-02-01 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vota', '0008_votacion_opcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcion',
            name='votos',
        ),
    ]
