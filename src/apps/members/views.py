from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView


from .forms import UserCreateForm
from apps.stories.models import Story


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


class MemberCreateView(CreateView):
    model = User
    template_name = 'members/form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('story:list')


class MemberDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = "members/profile.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        context['stories'] = Story.objects.filter(author=context['profile'].member)
        return context
