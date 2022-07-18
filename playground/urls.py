from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.say_hello),
    path('customers/', views.retrieveCustomers),
    path('customers/<str:surname>/', views.retrieveCustomer),
    path('customers/', views.createCustomer),
    path('customers/<str:surname>/', views.patchCustomer),
    path('customers/<str:surname>/', views.deleteCustomer),
]
