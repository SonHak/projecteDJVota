# Generated by Django 2.0 on 2018-01-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vota', '0002_auto_20180118_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vota.Consulta')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vota.Opcion')),
            ],
        ),
    ]
