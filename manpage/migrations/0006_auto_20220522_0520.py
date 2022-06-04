# Generated by Django 2.2.26 on 2022-05-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manpage', '0005_auto_20220514_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpagepost',
            name='distro',
            field=models.CharField(choices=[('blackarch', 'BlackArch'), ('centos', 'CentOS'), ('debian', 'Debian Linux'), ('freebsd', 'FreeBSD'), ('kali', 'Kali Linux'), ('macos', 'macOS'), ('parrot', 'Parrot OS'), ('qubes', 'Qubes OS'), ('raspberrypi', 'Raspberry Pi OS'), ('rhel', 'Red Hat Enterprise Linux'), ('slackware', 'Slackware'), ('ubuntu', 'Ubuntu Linux'), ('windows', 'Windows')], max_length=50, verbose_name='ディストロ'),
        ),
        migrations.AlterField(
            model_name='manpagepost',
            name='version',
            field=models.CharField(default=0.0, max_length=50, verbose_name='OS バージョン'),
        ),
    ]
