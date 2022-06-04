# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from manpage.models import ManpagePost
from pathlib import Path


#p = Path('../../templates/parrot/4.11/')
#html_list = p.glob('**/*.html')
#import pprint
#pprint.pprint(list(html_list))
#for i in html_list:
#    title = i.stem
#    print(title)

class Command(BaseCommand):
    args = ''
    help = 'This is custom command of Dejango. Useful howto page: https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database'
    
    def _insert_manpage_records(self):
#        p = Path('/home/daisuke/Documents/neoflowProject/manpage/templates/windows/ps/5.1.19041.1682/')
        p = Path('/home/daisuke/Documents/neoflowProject/manpage/templates/rhel/6.5/')
        html_list = p.glob('**/*.html')
        
        for i in html_list:
#            manpage = ManpagePost(title=i.stem, distro='windows', version='5.1.19041.1682(PowerShell)', content='なんぞこれ')
            manpage = ManpagePost(title=i.stem, distro='rhel', version='6.5', content='なんぞこれ')
            manpage.save()


    def handle(self, *args, **options):
        self._insert_manpage_records()