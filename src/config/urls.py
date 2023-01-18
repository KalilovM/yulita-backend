from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # admin
    path('admin/', admin.site.urls),
    # api
    path('api/', include('api.v1.urls')),
]
