from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_view(request):
    next_url = request.GET.get('next', '/')
    context = {}
    context['next_url'] = next_url
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next_url)
            else:
                context['errors'] = "User inactive"
                return render(request, "login.html", context)
        else:
            context['errors'] = "incorrect username or password"
            return render(request, "login.html", context)

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
