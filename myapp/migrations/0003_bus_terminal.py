# Generated by Django 3.2.6 on 2022-05-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220520_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='terminal',
            field=models.CharField(default=None, max_length=30),
        ),
    ]