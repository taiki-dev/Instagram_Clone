from django.urls import path
from .views import FormClass, ListClass

urlpatterns = [
    path('form/', FormClass.as_view(), name='form'),
    path('index/', ListClass.as_view(), name='index'),
]