from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import AcousticModel

def AboutGmm(request):
    return render(request, 'create_gmm/about_gmm.html')

class ModelCreateView(LoginRequiredMixin,CreateView):
    model = AcousticModel
    fields = ['model_name','audio_data','audio_format','sampling_rate']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AcousticModel
    fields = ['model_name','audio_data','audio_format','sampling_rate']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        model = self.get_object()
        if self.request.user == model.user:
            return True
        return False

class ModelDetailView(DetailView):
    model = AcousticModel

class ModelDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = AcousticModel
    success_url='/'
    def test_func(self):
        model = self.get_object()
        if self.request.user == model.user:
            return True
        return False

class ModelListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = AcousticModel
    template_name = 'create_gmm/modelsList.html'
    context_object_name = 'models'


