from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from django.urls import reverse_lazy

from .models import bookmark

class BookmarkListView(ListView):
    model = bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = bookmark

class BookmarkUpdateView(UpdateView):
    model = bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = bookmark
    success_url = reverse_lazy('list')

