from django.db import models
from datetime import datetime

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position =  models.ForeignKey(Position,
                on_delete=models.CASCADE,
                related_name='candidates',
                null=True, blank=True)
    birthdate = models.DateTimeField('Birthdate:')
    platform = models.TextField(max_length=200)


    def __str__(self):
        return 'Candidates: {}'. format(self.lastname, self.firstname, self.position)

class Vote(models.Model):
    candidate =  models.ForeignKey(Candidate,
                on_delete=models.CASCADE,
                related_name='votes')
    vote_datetime = models.DateTimeField(default=datetime.now)
