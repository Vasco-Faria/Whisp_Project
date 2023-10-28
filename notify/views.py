from django.shortcuts import render, redirect
from django.http import HttpResponse
from .notifications import get_unread_notifications_user, count_notififications_unread_user
from notifications.models import Notification
from django.urls import reverse
#from notifications.signals import notify

#def home(request):
    #notify.send(request.user, recipient=request.user, verb=f"Olá {request.user.email}, você acessou a pagina home.", description="Descricao de qualquer coisa")
    #return HttpResponse('Você está na home')


def listar_notificacoes(request):
    unread_notifications = get_unread_notifications_user(request.user)
    count = count_notififications_unread_user(request.user)
    return render(request, 'listar_notificacoes.html', {'unread_notifications': unread_notifications, 'count': count })


def marcar_notificao_como_lida(request):
    Notification.objects.mark_all_as_read(recipient=request.user)
    return redirect(reverse('listar_notificacoes'))
