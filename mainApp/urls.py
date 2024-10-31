from django.contrib import admin
from django.urls import path, include
from mainApp import views


urlpatterns = [
    path('', views.index, name='mainApp'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('sub', views.sub, name='sub'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('transactions', views.transaction_list, name='transaction_list'),

]