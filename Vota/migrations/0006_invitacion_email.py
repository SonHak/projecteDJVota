# Generated by Django 2.0 on 2018-01-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vota', '0005_auto_20180124_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitacion',
            name='email',
            field=models.CharField(default="manolo@nomail.com", max_length=200),
            preserve_default=False,
        ),
    ]