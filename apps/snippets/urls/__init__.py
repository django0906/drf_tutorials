from django.urls import path, include

urlpatterns = [
    path('django-fbv/', include('apps.snippets.urls.django_fbv')),
    path('drf-cbv/', include('apps.snippets.urls.drf_cbv')),
    path('drf-fbv/', include('apps.snippets.urls.drf_fbv')),
    path('drf-mixin/', include('apps.snippets.urls.drf_mixin')),
    path('drf-generics/', include('apps.snippets.urls.drf_generics')),
]
