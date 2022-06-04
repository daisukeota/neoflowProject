# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from manpage.models import ManpagePost


class Command(BaseCommand):
    args = ''
    help = 'some helpful description1'
    
    def _insert_manpage_records1(self):
        manpage = ManpagePost(title='diff',distro='parrot',version=4.11)
        manpage.save()


    def handle(self, *args, **options):
        self._insert_manpage_records1()