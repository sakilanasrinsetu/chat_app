# Generated by Django 3.2.8 on 2021-10-31 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(default='d', max_length=255),
            preserve_default=False,
        ),
    ]
