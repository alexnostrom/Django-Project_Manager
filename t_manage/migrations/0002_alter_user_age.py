# Generated by Django 4.2.2 on 2023-08-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
    ]
