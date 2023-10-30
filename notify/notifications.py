from notifications.models import Notification

def get_unread_notifications_user(user):
    unread_notifications = Notification.objects.unread().filter(recipient=user)
    return unread_notifications

def count_notififications_unread_user(user):
    return get_unread_notifications_user(user).count()

def get_read_notifications_user(user):
    read_notifications = Notification.objects.read().filter(recipient=user)
    return read_notifications