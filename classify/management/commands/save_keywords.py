# classify/management/commands/save_keywords.py

from django.core.management.base import BaseCommand
from classify.saveword import save_keywords_to_category_tables
import asyncio
import datetime

class Command(BaseCommand):
    help = 'Save keywords to category tables'

    def handle(self, *args, **kwargs):
        print("===================================")
        print(f"카테고리 - 현재시간: {datetime.now()}", end=", ")
        asyncio.run(save_keywords_to_category_tables())
        self.stdout.write(self.style.SUCCESS('Successfully saved keywords to category tables'))
