from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework.schemas import get_schema_view

from skeins import views as skein_views

router = DefaultRouter()
router.register(r"manufacturer", skein_views.ManufacturerViewset, basename="manufacturer")
router.register(r"colour", skein_views.ColourViewset, basename="colour")
router.register(r"fibre", skein_views.FibreViewset, basename="fibre")
router.register(r"skein", skein_views.SkeinViewset, basename="skein")

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.authtoken')),
    # path(
#         "openapi",
#         get_schema_view(title="Dates API", description="API", version="1.0.0"),
#         name="openapi-schema",
#     ),
]
