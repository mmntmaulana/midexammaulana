from django.forms import ModelForm
from .models import Candidate, Position


class CandidateUpdateForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']

class CandidateCreateForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']

class PositionCreateForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']
