# Generated by Django 3.2.7 on 2022-05-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_status_statusdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusdetails',
            name='send',
            field=models.IntegerField(),
        ),
    ]
