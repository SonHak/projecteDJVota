from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'Vota'
urlpatterns = [
	path('home', views.logearse),
    path('index' , views.IndexView.as_view(), name='index'),
   	path('loginUser', views.loginUser, name='loginUser'),
   	path('logoutUser', views.logoutUser, name='logoutUser'),
    path('<int:pk>/', views.ConsultaView.as_view(), name='consulta'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:consulta_id>/vota/', views.vota, name='vota')
]