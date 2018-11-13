from django.urls import path, include

urlpatterns = [
    path('django-fbv/', include('snippets.urls.django_fbv')),
    path('drf-fbv/', include('snippets.urls.drf_fbv')),
]
