from django.db import models

# Create your models here.
class ManpagePost(models.Model):
    DISTRO = (
        ('blackarch', 'BlackArch'),
        ('centos','CentOS'),
        ('debian','Debian Linux'),
        ('freebsd', 'FreeBSD'),
        ('kali','Kali Linux'),
        ('macos','macOS'),
        ('parrot','Parrot OS'),
        ('qubes','Qubes OS'),
        ('raspberrypi','Raspberry Pi OS'),
        ('rhel','Red Hat Enterprise Linux'),
        ('slackware', 'Slackware'),
        ('ubuntu','Ubuntu Linux'),
        ('windows','Windows'),
    )
    
    # title
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200
        )
    
    # content
    content = models.TextField(
        verbose_name = '本文'
        )
    
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True
        )
    
    distro = models.CharField(
        verbose_name = 'ディストロ',
        max_length=50,
        choices=DISTRO
        )
    
    version = models.CharField(
        verbose_name = 'OS バージョン',
        max_length=50,
        default = 0.0,
        )
    
    
    def __str__(self):
        return self.title
    
    