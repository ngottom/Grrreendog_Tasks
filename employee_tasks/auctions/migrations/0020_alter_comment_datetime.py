# Generated by Django 4.1.3 on 2022-12-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_comment_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.CharField(default='2022-12-07 15:47:01', max_length=100),
        ),
    ]
