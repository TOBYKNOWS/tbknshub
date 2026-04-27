from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),

    # Admin auth
    path('admin/login', views.admin_login, name='admin_login'),
    path('admin/logout', views.admin_logout, name='admin_logout'),

    # Admin pages
    path('admin', views.admin_dashboard, name='admin_dashboard'),
    path('admin/projects', views.admin_projects, name='admin_projects'),
    path('admin/clients', views.admin_clients, name='admin_clients'),
    path('admin/team', views.admin_team, name='admin_team'),
    path('admin/tasks', views.admin_tasks, name='admin_tasks'),
    path('admin/finance', views.admin_finance, name='admin_finance'),
    path('admin/messages', views.admin_messages, name='admin_messages'),

    # API
    path('api/stats', views.api_stats, name='api_stats'),
]
