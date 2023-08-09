from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:id>/', views.product, name='product'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_to_cart/', views.delete_to_cart, name='delete_to_cart'),
]