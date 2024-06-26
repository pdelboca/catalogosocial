from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("catalog/<int:pk>/", views.CatalogDetailView.as_view(), name="catalog"),
    path("catalog/<int:pk>/feed", views.feed, name="feed"),
    path(
        "distribution/<int:pk>/",
        views.DistributionDetailView.as_view(),
        name="distribution",
    ),
    path("search/", views.DatasetSearchView.as_view(), name="search"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("keyword/<slug:slug>/", views.KeywordSearchView.as_view(), name="keyword"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
