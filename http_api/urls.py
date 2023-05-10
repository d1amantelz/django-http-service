from django.urls import path
from http_api.views import index, get_cities, get_streets, shop_interface


urlpatterns = [
    path('', index),
    path('city/', get_cities, name='get_cities'),
    path('city/<int:city_id>/street/', get_streets, name='get_streets'),
    path('shop/', shop_interface, name='shop_interface'),
]
