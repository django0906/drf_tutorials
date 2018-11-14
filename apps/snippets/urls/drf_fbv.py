from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import django_fbv as views

urlpatterns = [
    path('snippets/', views.snippet_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
