# Generated by Django 4.0.3 on 2022-09-10 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0014_alter_siteinfo_siteconfig_name_cn'),
        ('rss', '0006_remove_rule_crontab_id_rule_job_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_name', models.CharField(max_length=500, verbose_name='种子名称')),
                ('seed_type', models.CharField(max_length=50, verbose_name='种子类型')),
                ('seed_details_link', models.URLField(blank=True, verbose_name='种子详情地址')),
                ('seed_published_time', models.DateField(verbose_name='发布时间')),
                ('seed_hash_id', models.CharField(max_length=50, verbose_name='种子hash值')),
                ('seed_donwload_link', models.URLField(blank=True, verbose_name='种子下载地址')),
                ('seed_file_size', models.IntegerField(verbose_name='种子文件大小')),
                ('seed_status', models.BooleanField(default=False, verbose_name='状态：下载，未下载')),
                ('photos', models.URLField(blank=True, verbose_name='海报')),
                ('douban_link', models.URLField(blank=True, verbose_name='豆瓣电影地址')),
                ('imdb_link', models.URLField(blank=True, verbose_name='IMDB电影地址')),
                ('siteinfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.siteinfo')),
            ],
        ),
    ]