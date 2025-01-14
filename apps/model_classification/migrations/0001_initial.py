# Generated by Django 4.1.7 on 2023-03-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=65, unique=True, verbose_name='模型名称')),
                ('model_describe', models.TextField(max_length=200, verbose_name='模型描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_use', models.BooleanField(default=False, verbose_name='是否使用')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '模型',
                'verbose_name_plural': '模型',
            },
        ),
    ]
