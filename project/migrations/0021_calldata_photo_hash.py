# Generated by Django 5.1.8 on 2025-04-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_calldata_mis1_calldata_mis2_calldata_mis3'),
    ]

    operations = [
        migrations.AddField(
            model_name='calldata',
            name='photo_hash',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
