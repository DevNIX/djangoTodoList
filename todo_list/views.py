# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from todo_list.models import List


def index(request):
    context = {}
    if request.user.is_authenticated():        # If the user is already logged
        context['page'] = 'todo-list'
        context['js'] = [
            'main.js'
        ]

    # Recuperamos las listas de tareas
    lists = List.get_list_and_task(request.user.id)

    context['lists'] = lists

    return render_to_response('base/main.html',
        context,
        RequestContext(request))


def login_user(request):
    if request.user.is_authenticated():        # If the user is already logged
        return redirect(reverse(index))
    else:
        context = {}                 # Variables for the template
        context['page'] = 'login'    # Login page

        if request.POST:        # Form is submitted?
            if request.POST.get('username', '') and request.POST.get('password', ''):
                login_data = {
                    'username': request.POST.get('username', ''),
                    'password': request.POST.get('password', '')
                }
                user = authenticate(**login_data)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse(index))
                    else:
                        context['error'] = 'blocked'
                else:
                    context['error'] = 'authentification'

        return render_to_response('base/main.html',
            context,
            RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect(reverse(index))
