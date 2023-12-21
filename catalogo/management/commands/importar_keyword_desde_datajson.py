import json

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from dcat.models import Catalog, Dataset, Keyword


class Command(BaseCommand):
    help = "Adds keywords to datasets from a DCAT data.json file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file", type=str, help="Path to the data.json file", default="data.json"
        )

    def handle(self, *args, **options):
        with open(options["file"]) as file:
            data = json.load(file)

        catalog_title = data["title"]
        catalog = Catalog.objects.get(title=catalog_title)

        for dataset in data["dataset"]:
            identifier = dataset["identifier"]
            dataset_obj = Dataset.objects.get(
                extras__original_id=identifier, catalog=catalog
            )

            for keyword in dataset["keyword"]:
                keyword_obj, _ = Keyword.objects.get_or_create(
                    name=keyword, slug=slugify(keyword)
                )
                if keyword_obj in dataset_obj.keywords.all():
                    self.stdout.write(
                        self.style.WARNING(
                            f"Keyword {keyword} already exists in dataset {dataset_obj.title}. Skipping..."
                        )
                    )
                    continue
                dataset_obj.keywords.add(keyword_obj)

        self.stdout.write(self.style.SUCCESS("Keywords added successfully"))
