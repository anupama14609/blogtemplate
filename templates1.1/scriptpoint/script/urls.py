from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('analyze-url', views.AnalyzeUrl, name='analyze-url'),
    path('generate-password', views.GeneratePassword, name='generate-password'),
    path('generate-meta', views.GenerateMeta, name='generate-meta'),
    path('location-finder', views.LocationFinder, name='location-finder'),

]