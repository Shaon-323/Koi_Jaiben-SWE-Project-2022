# Generated by Django 3.2.6 on 2022-05-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
