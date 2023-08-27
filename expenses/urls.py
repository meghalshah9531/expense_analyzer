from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('records/', views.records_view, name='records'),
    path('imports/', views.imports_view, name='imports'),
    path('analytics/', views.analytics_view, name='analytics'),
]
