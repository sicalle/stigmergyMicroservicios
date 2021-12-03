from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def home1(request):
    return HttpResponse("Welcome to my web site")

def home(request):
    now = datetime.now()

    html_content = "<html><head><title>Hello, Django</title></head><body>"
    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse(html_content)

def logout_view(request):
    logout(request)
    return HttpResponse("Sesión cerrada!")