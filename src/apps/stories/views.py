from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,\
    DeleteView, DetailView


from .models import Story


class StoryListView(ListView):
    context_object_name = "stories"
    model = Story
    template_name = "stories/list.html"


class StoryDetailView(DetailView):
    context_object_name = "story"
    template_name = "stories/story.html"
    model = Story


class StoryCreateView(CreateView):
    template_name = "stories/form.html"
    model = Story
    fields = ['name', 'description', 'category']
    success_url = reverse_lazy('story:list')


class StoryUpdateView(UpdateView):
    template_name = "stories/form.html"
    model = Story
    fields = ['name', 'description', 'category']
    success_url = reverse_lazy('story:list')


class StoryDeleteView(DeleteView):
    model = Story
    success_url = reverse_lazy('story:list')
