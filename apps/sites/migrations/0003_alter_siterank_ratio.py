# Generated by Django 4.0.2 on 2022-02-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_siterank_up_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siterank',
            name='ratio',
            field=models.CharField(max_length=20, verbose_name='分享率'),
        ),
    ]
