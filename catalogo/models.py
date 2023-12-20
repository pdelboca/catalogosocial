from django.db import models
from dcat.models import Dataset, Distribution


class DatasetExtras(models.Model):
    dataset = models.OneToOneField(
        Dataset, on_delete=models.CASCADE, related_name="extras"
    )
    original_landing_page = models.URLField(blank=True, null=True)
    original_id = models.CharField(max_length=255, blank=True)


class DistributionExtras(models.Model):
    distribution = models.OneToOneField(
        Distribution, on_delete=models.CASCADE, related_name="extras"
    )
    original_access_url = models.URLField(blank=True, null=True)
    original_download_url = models.URLField(blank=True, null=True)
    original_id = models.CharField(max_length=255, blank=True)
