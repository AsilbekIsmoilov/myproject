# Generated by Django 5.2 on 2025-04-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_alter_calldata_dialog1_alter_calldata_dialog10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calldata',
            name='mis1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calldata',
            name='mis2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calldata',
            name='mis3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
