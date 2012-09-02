# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def index(request):
    context = {}

    if request.POST.get('username', '') and request.POST.get('password', ''):
        login_data = {
            'username': request.POST.get('username', ''),
            'password': request.POST.get('password', '')
        }
        user = authenticate(username = login_data['username'], password = login_data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)

    return render_to_response('base/header.html',
        context,
        RequestContext(request))


def logoutAction(request):
    logout(request)
    return redirect(reverse(index))
