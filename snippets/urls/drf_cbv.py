from django.urls import path

from ..views import drf_cbv as views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view())
]
