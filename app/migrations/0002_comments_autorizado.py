# Generated by Django 2.2.3 on 2019-07-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='autorizado',
            field=models.BooleanField(default=False, verbose_name='Autorizado?'),
        ),
    ]