from django.urls import path
from .views import ExchangeView


urlpatterns = [
    path('', ExchangeView.as_view(), name="exchange")

]
