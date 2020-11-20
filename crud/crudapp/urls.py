from django.urls import path
from . import views

urlpatterns = [
    path('', views.crudapp, name='crudapp'),
    path('crudbu')

]
