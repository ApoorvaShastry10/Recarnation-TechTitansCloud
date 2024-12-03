from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('sell', views.sell, name='sell'),
    path('predict', views.predict, name='predict'),
    path('contact', views.contact, name='contact')
]
