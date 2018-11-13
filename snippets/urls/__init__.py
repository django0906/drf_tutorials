from django.urls import path, include

urlpatterns = [
    path('django-fbv/', include('snippets.urls.django_fbv')),
    path('drf-cbv/', include('snippets.urls.drf_cbv')),
    path('drf-fbv/', include('snippets.urls.drf_fbv')),
    path('drf-mixin/', include('snippets.urls.drf_mixin')),
    path('drf-generics/', include('snippets.urls.drf_generics')),
]
