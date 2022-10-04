from django.urls import path

from todo_app import views

app_name = 'todo_app'

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Task_listview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Task_detailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Task_updateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Task_deleteview.as_view(), name='cbvdelete'),

]