
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title = "Book List Api",
        default_version = "v1",
        description = "library demo project",
        terms_of_service = "demo.com",
        contact = openapi.Contact(email = "musabekmusayev98@gmail.com"),
        license = openapi.License(name = "demo Lisence"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    #swagger
    path('swagger<format>/', scheme_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', scheme_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', scheme_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]

