
from django.urls import path


from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('food/', views.food_list, name='food_list'),
    path('food/create/', views.food_create, name='food_create'),
    path('food/update/<int:pk>/', views.food_update, name='food_update'),
    path('food/detail/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/delete/<int:pk>/', views.food_delete, name='food_delete'),
    path('foodwaste/', views.foodwaste_list, name='foodwaste_list'),
    path('foodwaste/create/', views.foodwaste_create, name='foodwaste_create'),
    path('foodwaste/update/<int:pk>/', views.foodwaste_update, name='foodwaste_update'),
    path('foodwaste/detail/<int:pk>/', views.foodwaste_detail, name='foodwaste_detail'),
    path('foodwaste/delete/<int:pk>/', views.foodwaste_delete, name='foodwaste_delete'),
    path('foodcategory/', views.foodcategory_list, name='foodcategory_list'),
    path('foodcategory/create/', views.foodcategory_create, name='foodcategory_create'),
    path('foodcategory/update/<int:pk>/', views.foodcategory_update, name='foodcategory_update'),
    path('foodcategory/<int:pk>/', views.foodcategory_detail, name='foodcategory_detail'),
    path('foodcategory/delete/<int:pk>/', views.foodcategory_delete, name='foodcategory_delete'),
    path('wastecategory/', views.wastecategory_list, name='wastecategory_list'),
    path('wastecategory/create/', views.wastecategory_create, name='wastecategory_create'),
    path('wastecategory/update/<int:pk>/', views.wastecategory_update, name='wastecategory_update'),
    path('wastecategory/<int:pk>/', views.wastecategory_detail, name='wastecategory_detail'),
    path('wastecategory/delete/<int:pk>/', views.wastecategory_delete, name='wastecategory_delete'),
] 
