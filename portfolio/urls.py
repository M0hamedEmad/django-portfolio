from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_project/', views.create_project, name='create-project'),
    path('update_project/<int:pk>.', views.updateProject, name='update-project'),
    path('delete_project/<int:pk>/', views.deleteProject, name='delete-project'),
    path('activesection/', views.activeSection, name='active-section'),
]