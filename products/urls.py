from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'products-api', ProductViewSet)

urlpatterns = [
    path("", product_list, name='home'),
    path('create-product/', create_product, name='create-product'),
    path('update-product/<str:pk>', update_product, name='update-product'),
    path('delete-product/<str:pk>', delete_product, name='delete-product'),

    path('get-product/', get_a_product, name="get_a_product"),
    path('api/product/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='productapi_rest_framework'))
]