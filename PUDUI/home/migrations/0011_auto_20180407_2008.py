# Generated by Django 2.0.3 on 2018-04-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_communication_is_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_appointment',
            name='health_instance',
        ),
        migrations.AddField(
            model_name='doctor_appointment',
            name='health_instance',
            field=models.ManyToManyField(default=0, to='home.health_instance'),
        ),
    ]
