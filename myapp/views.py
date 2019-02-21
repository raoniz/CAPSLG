from django.http import HttpResponseRedirect
from django.shortcuts import render
from rebar.testing import flatten_to_dict
from .algorithms import predict_proba
import numpy as np

from .models import UserForm

def index(request):
    flag = False
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            flag = True
            form_data = flatten_to_dict(form)
            filename = '../data/pickles/' + form_data['college'] + '.pkl'
            test = np.array([2019, form_data['branch'], form_data['category'], form_data['score']])
            form_data['probability'] = predict_proba.main(filename, test)

            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            return render(request, 'index.html', {'form': form, 'form_data': form_data, 'flag': flag})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form, 'flag': flag})

def userPreference(request):
    return render(request, 'user_preference.html')

def smartList(request):
    return render(request, 'smart_list.html')
