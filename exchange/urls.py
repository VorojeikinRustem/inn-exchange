from django.urls import path
from .views import make_exchange_great_again


urlpatterns = [
    path('', make_exchange_great_again, name="exchange")

]
