# Generated by Django 2.0.3 on 2018-04-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180407_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]