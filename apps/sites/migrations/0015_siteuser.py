# Generated by Django 4.1 on 2022-09-15 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0014_alter_siteinfo_siteconfig_name_cn'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('uid', models.IntegerField(verbose_name='用户ID号')),
                ('create_time', models.DateTimeField(verbose_name='账号创建时间')),
                ('ratio', models.CharField(max_length=20, verbose_name='分享率')),
                ('upload', models.CharField(max_length=50, verbose_name='上传量')),
                ('download', models.CharField(max_length=50, verbose_name='下载量')),
                ('bonus', models.CharField(max_length=50, verbose_name='魔力值')),
                ('score', models.CharField(max_length=50, verbose_name='积分')),
                ('level', models.CharField(max_length=20, verbose_name='等级')),
                ('published_seed_num', models.IntegerField(verbose_name='发种数量')),
                ('seed_num', models.IntegerField(verbose_name='做种数量')),
                ('siteinfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.siteinfo')),
            ],
        ),
    ]