from django.urls import path

from ..views import django_fbv as views

urlpatterns = [
    path('snippets/', views.snippet_list),
]
