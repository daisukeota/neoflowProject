# Generated by Django 2.2.26 on 2022-05-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manpage', '0002_auto_20220514_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='manpagepost',
            name='version',
            field=models.IntegerField(default=4.11, verbose_name='OS バージョン'),
            preserve_default=False,
        ),
    ]
