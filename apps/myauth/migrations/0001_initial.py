# Generated by Django 3.1.7 on 2021-03-26 03:36

from django.db import migrations, models
import myauth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mymenu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='name')),
                ('tag', models.CharField(default='unknow', max_length=30, verbose_name='用于业务识别标签')),
                ('permissions', models.ManyToManyField(blank=True, to='mymenu.Menu', verbose_name='permissions')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            managers=[
                ('objects', myauth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=30, verbose_name='真实姓名')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='邮箱')),
                ('is_delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('avatar', models.URLField(blank=True, verbose_name='头像')),
                ('mobile', models.CharField(max_length=15, null=True, verbose_name='移动电话')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='myauth.Group', verbose_name='groups')),
                ('permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='mymenu.Menu', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
