# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'manpage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path( 'blackarch/', views.BlackarchView.as_view(), name='blackarch'),
    path( 'centos/', views.CentosView.as_view(), name='centos' ),
    path( 'contact/', views.ContactView.as_view(), name='contact' ),
    path( 'debian/', views.DebianView.as_view(), name='debian' ),
    path( 'deepin/', views.DeepinView.as_view(), name='deepin' ),
    path( 'detail/<int:pk>/', views.ManpageDetail.as_view(), name='manpage_detail' ),
    path( '<str:distro>/<str:version>/<str:title>/', views.ManpageDetail.as_view(), name='manpage_url' ),
    path( 'freebsd/', views.FreebsdView.as_view(), name='freebsd' ),
    path( 'kali/', views.KaliView.as_view(), name='kali' ),
    path( 'macos/', views.MacosView.as_view(), name='macos' ),
    path( 'parrot/', views.ParrotView.as_view(), name='parrot' ),
    path( 'qubes/', views.QubesView.as_view(), name='qubes' ),
    path( 'raspberrypi/', views.RaspberrypiView.as_view(), name='raspberrypi' ),
    path( 'rhel/', views.RhelView.as_view(), name='rhel' ),
    path( 'slackware/', views.SlackwareView.as_view(), name='slackware'),
    path( 'ubuntu/', views.UbuntuView.as_view(), name='ubuntu' ),
    path( 'windows/', views.WindowsView.as_view(), name='windows' ),
]
