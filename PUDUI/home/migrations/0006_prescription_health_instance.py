# Generated by Django 2.0.3 on 2018-04-07 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='health_instance',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.health_instance'),
        ),
    ]
