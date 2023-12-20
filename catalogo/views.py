from django.db.models import Q
from django.views import generic

from dcat.models import Catalog, Dataset, Distribution


# Create your views here.
class IndexView(generic.ListView):
    template_name = "portal/index.html"
    context_object_name = "catalogs"

    def get_queryset(self):
        """Return the last five published questions."""
        return Catalog.objects.all()

    def get_context_data(self, **kwargs):
        """Returns a list of Catalog objects.

        It also returns the total number of datasets and distributions.
        """
        context = super().get_context_data(**kwargs)
        catalogs = context["catalogs"]
        context["catalogs"] = catalogs
        context["datasets"] = Dataset.objects.count()
        context["distributions"] = Distribution.objects.count()
        return context

def _dataset_contains_queryset(q):
    """Returns dataset queryset filtered by q

    It returns all dataset that contains q in the title or description
    and all datasets with distributions containing q in the title or description.
    """
    # Get all distributions containing q
    distributions = Distribution.objects.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
    _pks = [d.dataset.pk for d in distributions]

    # Get datasets containing q or matching pks of distributions' dataset
    datasets = Dataset.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q) | Q(pk__in=_pks)
    )
    return datasets


class CatalogDetailView(generic.DetailView):
    model = Catalog
    template_name = "portal/catalog.html"

    def get_context_data(self, **kwargs):
        """Returns a Catalog object and filtered datasets."""
        context = super().get_context_data(**kwargs)
        catalog = context["catalog"]
        q = self.request.GET.get("q")
        if q:
            datasets = _dataset_contains_queryset(q).filter(catalog=catalog)
        else:
            datasets = Dataset.objects.filter(catalog=catalog)
        context["datasets"] = datasets.prefetch_related('distribution_set', 'distribution_set__format')
        return context


class DistributionDetailView(generic.DetailView):
    model = Distribution
    template_name = "portal/distribution.html"


class DatasetSearchView(generic.ListView):
    template_name = "portal/search.html"
    context_object_name = "datasets"

    def get_queryset(self):
        """Returns a list of filtered datasets.

        It filters by title and description of the dataset and its distributions.
        """
        q = self.request.GET.get("q")
        if q:
            datasets = _dataset_contains_queryset(q)
        else:
            datasets = Dataset.objects.all()
        return datasets.prefetch_related('distribution_set', 'distribution_set__format')
