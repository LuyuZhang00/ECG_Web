# Generated by Django 4.1.7 on 2023-03-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormanage',
            name='doctor_age',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='医生年龄'),
        ),
    ]