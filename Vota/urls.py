from django.urls import path

from . import views

app_name = 'Vota'
urlpatterns = [
    path('' , views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ConsultaView.as_view(), name='consulta'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:consulta_id>/vota/', views.vota, name='vota')
]