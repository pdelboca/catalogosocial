from django.db import models
from dcat.models import Dataset, Distribution


class DatasetExtras(models.Model):
    dataset = models.OneToOneField(
        Dataset, on_delete=models.CASCADE, related_name="extras"
    )


class DistributionExtras(models.Model):
    distribution = models.OneToOneField(
        Distribution, on_delete=models.CASCADE, related_name="extras"
    )
