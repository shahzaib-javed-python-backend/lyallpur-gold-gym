"""
URL configuration for gymManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='home'),
    path('dashboard/', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('enquiry/add/', views.enquiry_add, name='enquiry_add'),
    path('enquiry/', views.enquiry_list, name='enquiry_list'),
    path('enquiry/<int:enquiry_id>/delete/', views.enquiry_delete, name='enquiry_delete'),
    path('plans/add/', views.plan_add, name='plan_add'),
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/<int:plan_id>/delete/', views.plan_delete, name='plan_delete'),
    path('equipment/add/', views.equipment_add, name='equipment_add'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:equipment_id>/delete/', views.equipment_delete, name='equipment_delete'),
    path('members/add/', views.member_add, name='member_add'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/delete/', views.member_delete, name='member_delete'),
]
