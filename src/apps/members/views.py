from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView


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


class MemberDetailView(ListView):
    context_object_name = "stories"
    template_name = "members/profile.html"

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.args[0])
        return Story.objects.filter(author=self.author.member)
