from django.shortcuts import render
from django.views.generic import ListView

from works.models import WorksModel


class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
