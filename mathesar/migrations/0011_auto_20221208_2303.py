# Generated by Django 3.1.14 on 2022-12-08 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0010_auto_20221208_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_change_needed',
            field=models.BooleanField(default=False),
        ),
    ]
