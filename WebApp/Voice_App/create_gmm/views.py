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
from django.http import HttpResponse, HttpResponseRedirect

class ModelCreateView(LoginRequiredMixin,CreateView):
    model = AcousticModel
    fields = ['model_name','audio_data','audio_format','sampling_rate']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModelUpdateView(LoginRequiredMixin, UpdateView):
    model = AcousticModel
    fields = ['model_name','audio_data','audio_format','sampling_rate']

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)

class ModelDetailView(DetailView):
    model = AcousticModel
