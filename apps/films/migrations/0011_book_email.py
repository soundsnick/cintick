# Generated by Django 2.2.6 on 2019-11-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_seance_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.CharField(default='Null value', max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
