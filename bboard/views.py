import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Bb, Rubric
from .forms import BbForm


def index(request):
    year = datetime.datetime.now()
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs,
               'rubrics': rubrics,
               'date': year.strftime("%Y")
               }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    year = datetime.datetime.now()
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.filter(id=rubric_id).first()
    context = {'bbs': bbs,
               'rubrics': rubrics,
               'current_rubric': current_rubric,
               'date': year.strftime("%Y")
               }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = datetime.datetime.now()
        context['rubrics'] = Rubric.objects.all()
        context['date'] = year.strftime("%Y")
        return context
