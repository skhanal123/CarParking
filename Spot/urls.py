from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

######### Swagger Configuration Starts Here ########
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Pricing API",
      default_version='v1',
      description="Pricing API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
######### Swagger Configuration Ends Here ########

######### Router Configuration Starts Here ########

router = DefaultRouter()
router.register('rates', views.parkingRateViewset, basename = 'rates')

######### Router Configuration Starts Here ########


urlpatterns = [
    path('admin/', admin.site.urls),                                              # This url leads you to admin page
    path('', views.JsonData),                                                     # This url leads you to home page for automatic json file upload 
    path('api/price', views.priceapi),                                            # This url is for price api endpoint
    path('api/', include(router.urls)),                                           # This url is for rates api endpoint
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # This url is for swagger
]
