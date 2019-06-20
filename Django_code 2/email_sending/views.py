from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage, send_mass_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string


def send_email(request):
    file = ''
    # content = file.read()
    message = render_to_string('genrate_mail.txt', {
        'sender_name': 'Pranjal Kushawaha',
        'mess': 'Test Mail',
    })
    users = User.objects.all()

    # Send Email separately
    for i in users:
        send_mail('Testing Mail Send Separately', message, settings.EMAIL_HOST_USER, [i.email])

    # Send Email with Document
    for i in users:
        email = EmailMessage('Testing Mail With Document', message, to=[i.email])
        # email.attach(file.name, content, 'application/pdf')
        email.send()

    # Send Mass Email
    email_list = []
    for i in users:
        email = ('Testing Mail Sending Mass Mail', message, settings.EMAIL_HOST_USER, [i.email])
        email_list.append(email)
    t = tuple(email_list)
    send_mass_mail(t, fail_silently=False)
    return redirect('home')
