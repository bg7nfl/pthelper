# Generated by Django 4.0.3 on 2022-08-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0005_delete_notifytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifyconfig',
            name='enwechat_agent_id',
            field=models.CharField(default='', max_length=50, verbose_name='应用ID'),
        ),
        migrations.AddField(
            model_name='notifyconfig',
            name='enwechat_agent_secret',
            field=models.CharField(default='', max_length=200, verbose_name='应用密钥'),
        ),
        migrations.AddField(
            model_name='notifyconfig',
            name='enwechat_corp_id',
            field=models.CharField(default='', max_length=100, verbose_name='企业ID'),
        ),
        migrations.AlterField(
            model_name='notifyconfig',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='名称,特定:iyuu,telegram,email,enwechat'),
        ),
        migrations.AlterField(
            model_name='notifyconfig',
            name='receive_user',
            field=models.CharField(max_length=200, verbose_name='接收账号,默认为发信账号,企业微信接收者'),
        ),
    ]
