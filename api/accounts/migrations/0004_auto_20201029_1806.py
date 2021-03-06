# Generated by Django 3.1.2 on 2020-10-29 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201029_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connections',
            options={'verbose_name': 'Connection', 'verbose_name_plural': 'Connections'},
        ),
        migrations.AlterField(
            model_name='connections',
            name='follower',
            field=models.ManyToManyField(blank=True, null=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='connections',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
