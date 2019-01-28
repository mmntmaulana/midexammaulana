from django.shortcuts import render
from django.http import HttpResponse
from .models import Position, Candidate, Vote
from .forms import CandidateCreateForm
from .forms import CandidateUpdateForm
from .forms import PositionCreateForm

# Create your views here.

def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)


def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html', context)

def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        form = CandidateUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate Updated')
        else:
            context['form'] = form
            render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateUpdateForm(instance=post)
        return render(request, 'candidate_update.html', context)

def candidate_create(request):

    context = {}
    form = CandidateCreateForm()

    if request.method == 'POST':
        form = CandidateCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate Created')

    return render(request, 'candidate_create.html', {'form': form})

def position_create(request):

    context = {}
    form = PositionCreateForm()

    if request.method == 'POST':
        form = PositionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Position Created')

    return render(request, 'position_create.html', {'form': form})
