# Generated by Django 5.1.8 on 2025-05-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0047_get_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_reports',
            name='call_code',
            field=models.BigIntegerField(),
        ),
    ]
