from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_img', views.predict, name='prediction'),
]
