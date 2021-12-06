from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def home1(request):
    return HttpResponse("Welcome to my web site")


def logout_view(request):
    logout(request)
    return HttpResponse("Sesión cerrada!")