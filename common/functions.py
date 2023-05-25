import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.core.mail import send_mail,EmailMessage

def from_email():
    return 'm-sales@mifumotz.com'


def send_mail(to,subject,msg):
        email = EmailMessage(
        subject=subject,
        body=msg,
        from_email=from_email(),
        to=[to],
        cc=['eliezer.kyomo@mifumotz.com'],
        reply_to=['ab@mifumotz.com'],
        headers={'Message-ID': 'ABD'},
        )
        email.content_subtype = "html"
        return email.send(fail_silently=True)

