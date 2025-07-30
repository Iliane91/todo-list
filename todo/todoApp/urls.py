from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil/', views.accueil, name='accueil'),
    path('about-us/', views.about_us, name='about-us'),
    path('todo-list/', views.todo_list, name='todo-list'),
    path('todo-list/add/', views.task_create, name='task-create'),
    path('task-details/<int:task_id>/', views.task_details, name='task-details'),
    path('task-details/<int:task_id>/update/', views.task_update, name='task-update'),
    path('task-details/<int:task_id>/delete/', views.task_delete, name='task-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='todoApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
]