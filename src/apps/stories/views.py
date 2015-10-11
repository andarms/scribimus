from django.shortcuts import render
from django.views.generic import CreateView, ListView


from .models import Story


def home(request):
    return render(request, "home.html", {})


class StoryListView(ListView):
    template_name = "stories/list.html"
    model = Story


class StoryCreateView(CreateView):
    template_name = "stories/create.html"
    model = Story
    fields = ['name', 'description', 'category']
    success_url = '/story/'
