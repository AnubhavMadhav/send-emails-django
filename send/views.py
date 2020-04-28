from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('This is Subject',
              'Hello!! This is an automated mail, sent using django.',
              'senders-email-address',
              ['recipient-1-mail-address','recipient-2-mail-address', 'recipient-3-mail-address', 'recipient-4-mail-address'],
              fail_silently=False)
    return render(request, "send/index.html")