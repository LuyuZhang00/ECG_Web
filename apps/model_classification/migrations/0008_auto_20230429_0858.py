# Generated by Django 2.2.28 on 2023-04-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_classification', '0007_alter_modelmanage_model_describe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmanage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
