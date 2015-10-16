from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView,\
    DeleteView, DetailView, TemplateView


from .models import Story, StoryCategory
from core.mixins import LoginRequiredMixin


class StoryListView(ListView):
    context_object_name = "stories"
    model = Story
    template_name = "stories/list.html"


class StoryDetailView(DetailView):
    context_object_name = "story"
    template_name = "stories/story.html"
    model = Story


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = "stories/form.html"
    model = Story
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy('stories:list')

    def get_form_kwargs(self):
        kwargs = super(StoryCreateView, self).get_form_kwargs()
        if 'data' in kwargs:
            instance = Story(author=self.request.user.member)
            kwargs.update({'instance': instance})
        return kwargs


class StoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "stories/form.html"
    model = Story
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy('stories:list')


class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Story
    success_url = reverse_lazy('stories:list')


class StoryCategoryListView(ListView):
    context_object_name = "stories"
    template_name = "stories/list.html"

    def get_queryset(self):
        self.category = get_object_or_404(StoryCategory, name=self.args[0])
        return Story.objects.filter(category=self.category)


class ExploreView(TemplateView):
    template_name = "stories/explore"
