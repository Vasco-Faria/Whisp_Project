from django.urls import path
from . import views


app_name="notify"

urlpatterns = [
    #path('home/', views.home, name="home"),
    path("", views.listar_notificacoes, name="listar_notificacoes"),
    path('marcar_notificao_como_lida/', views.marcar_notificao_como_lida, name='marcar_notificao_como_lida'),
]   