from django.urls import path 

from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('delete-todo/<str:pk>/', views.deleteTodo, name='delete-todo'),
    path('complete-todo/<str:pk>/', views.CompleteTodo, name='complete-todo'),
    path('undocomplete-todo/<str:pk>/', views.undoComplete, name='undocomplete-todo'),
    path('update-todo/<str:pk>/', views.updateTodos, name='updatetodo'),

    path('signup/', views.signUp, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('log-out/', views.logoutUser, name='log-out'),

]

