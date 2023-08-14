from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ronnel', views.ronnel, name='ronnel'),
    path('ning', views.ning, name='ning'),
    path('<str:name>', views.greet, name='greet')
]