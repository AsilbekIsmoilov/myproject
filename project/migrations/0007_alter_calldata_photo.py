# Generated by Django 5.2 on 2025-04-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_calldata_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldata',
            name='photo',
            field=models.ImageField(max_length=500, null=True, upload_to=''),
        ),
    ]
