# Generated by Django 5.0.7 on 2024-07-15 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('zbiórka lokalna', 'zbiórka lokalna'), ('fundacja', 'fundacja'), ('organizacja porządkowa', 'organizacja porządkowa')], default='fundacja', max_length=100)),
                ('categories', models.ManyToManyField(to='myapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('adress', models.TextField()),
                ('phone_number', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.TextField()),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='myapp.category')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('institution', models.ManyToManyField(to='myapp.institution')),
            ],
        ),
    ]
