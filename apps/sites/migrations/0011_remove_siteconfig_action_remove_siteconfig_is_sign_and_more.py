# Generated by Django 4.0.2 on 2022-03-01 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_siteconfig_is_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfig',
            name='action',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='is_sign',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='sign_url',
        ),
    ]