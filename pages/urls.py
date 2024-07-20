#coloco la urls para decirle a Django la dir
from django.urls import path
from .views import HomePageView
urlpatterns =[
    path("",HomePageView.as_view(), name = 'home'),
]