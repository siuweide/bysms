# Generated by Django 2.1 on 2020-08-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200811_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='create_data',
            new_name='create_time',
        ),
        migrations.AddField(
            model_name='order',
            name='medicinelist',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]