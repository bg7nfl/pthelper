# Generated by Django 4.0.2 on 2022-02-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0003_notifyconfig_mail_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='类型名称,QQ邮箱')),
                ('alias_name', models.CharField(max_length=20, verbose_name='类型别名,qq,sina,163')),
                ('smtp_server', models.CharField(max_length=100, verbose_name='发信地址')),
                ('smtp_port', models.IntegerField(default=465, verbose_name='发信端口')),
            ],
        ),
        migrations.RemoveField(
            model_name='notifyconfig',
            name='smtp_is_tls',
        ),
        migrations.RemoveField(
            model_name='notifyconfig',
            name='smtp_port',
        ),
        migrations.RemoveField(
            model_name='notifyconfig',
            name='smtp_server',
        ),
    ]
