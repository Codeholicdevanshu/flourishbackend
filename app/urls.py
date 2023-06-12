from django.urls import path,include
from .views import *
from app import views
urlpatterns = [
   path('api/country',CountryView.as_view(),name='country'),
   path('',views.index,name='index')
]

