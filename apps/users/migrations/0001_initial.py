# Generated by Django 2.2.6 on 2019-11-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
            ],
        ),
    ]
