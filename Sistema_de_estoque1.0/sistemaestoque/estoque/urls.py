from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.estoque_home, name="home"),
    path("adicionar/", views.estoque_adicionar, name="adicionar"),
    path("remover/<int:id>/", views.estoque_remover, name="remover"),
    path("editar/<int:id>/", views.estoque_editar, name="editar"),
    path('entrada/<int:item_id>/', views.registrar_entrada, name='registrar_entrada'),
    path('saida/<int:item_id>/', views.registrar_saida, name='registrar_saida'),
    path('social/', views.pagina_social, name='pagina_social'),
    path("historico/", views.historico, name="historico"),
]


