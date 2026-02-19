from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post,Categories


class Command(BaseCommand):
    help = "populate the category data"
   
    def handle(self, *args: Any, **options: Any):
        Categories.objects.all().delete()
        categories = ["sports","technology","science","art","food"]

        for name in categories:
            Categories.objects.get_or_create(name=name)

            

        self.stdout.write(
            self.style.SUCCESS("Categories Created Successfully ✅")
        )
