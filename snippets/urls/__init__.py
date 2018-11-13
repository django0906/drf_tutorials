from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('django-fbv/', include('snippets.urls.django_fbv')),
    path('drf-fbv/', include('snippets.urls.drf_fbv')),
]

urlpatterns = format_suffix_patterns(urlpatterns)