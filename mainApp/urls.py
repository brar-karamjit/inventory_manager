from django.contrib import admin
from django.urls import path, include
from mainApp import views


urlpatterns = [
    path('', views.index, name='mainApp'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('barcodescan/', views.barcodescan),
    path('products/', views.products, name='products'),
    path('sub/', views.sub, name='sub'), # remove from quantity
    path('returnitem/', views.returnitem, name='returnitem'), # Add to quantity
    path('additem/', views.additem, name='additem'), # Add new item
    path('delete/', views.delete, name='delete'), # Delete item
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail')

]