from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="FizzBuzz API",
        default_version="v1",
        description="API endpoints for the FizzBuzz API",
        contact=openapi.Contact(email="jonathan_constantn@outlook.com.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('admin/', admin.site.urls),
    path("api/v1/", include("core_apps.fizzbuzz_creator.urls")),
    path('api/', include('rest_framework.urls'))
]
