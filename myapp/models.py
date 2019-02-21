from django.db import models
from django import forms

# Create your models here.
CATEGORY_CHOICES = (
    ('GOPEN', 'Open'),
    ('sc', 'Scheduled Caste'),
    ('st', 'Scheduled Tribe'),
)

BRANCH_CHOICES = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
)

COLLEGE_CHOICES = (
    ('vjti', 'VJTI'),
    ('spcoe', 'SPCOE'),
    ('kjsce', 'KJSCE'),
)

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=15, widget=forms.Select(choices=CATEGORY_CHOICES))
    score = forms.IntegerField()
    college = forms.CharField(max_length=15, widget=forms.Select(choices=COLLEGE_CHOICES))
    branch = forms.CharField(max_length=15, widget=forms.Select(choices=BRANCH_CHOICES))
