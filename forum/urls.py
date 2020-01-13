from django.urls import include, path

from forum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create),
    path('category/<str:pk>/', views.category_page, name='category_page'),
    path('send_message/', views.send_message, name='send_message'),
    path('zapros/', views.zapros, name='zapros'),

]
