# Generated by Django 3.2 on 2021-05-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210429_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phno', models.CharField(default='', max_length=70)),
                ('descr', models.CharField(default='', max_length=50)),
            ],
        ),
    ]