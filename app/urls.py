from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<slug:slug>',views.detail,name='detail'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('region/<slug:slug>/', views.region_filter, name="region"),
    path('category/<slug:slug>/', views.category, name="category"),
]