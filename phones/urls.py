from django.urls import path 

from .views import PhonesView


urlpatterns = [
    path('', PhonesView.as_view(), name='phones'),
]

