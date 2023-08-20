"""
URL configuration for AdminPanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Panel.views import FoodListView, AddFoodView, FoodDetailView, FoodDeleteView, FoodUpdateView

urlpatterns = [
    path('', FoodListView.as_view(), name='index'),
    path('/addFood/', AddFoodView.as_view(), name='add_food'),
    path('/detail/<slug:slug_param>/', FoodDetailView.as_view(), name='food_detail'),
    path('/delete/<slug:slug_param>/', FoodDeleteView.as_view(), name='delete_food'),
    path('/update/<slug:slug_param>/', FoodUpdateView.as_view(), name='update_food'),
    path('admin/', admin.site.urls),
]
