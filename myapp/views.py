from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rebar.testing import flatten_to_dict
from .algorithms import predict_proba, generate_list
import numpy as np
import pickle
import json

from .models import UserForm, PredictCollege, CollegeData

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
            filename = 'myapp/data/pickles/colleges/' + form_data['college'] + '.pkl'
            test = np.array([2019, form_data['branch'], form_data['category'], form_data['score']])
            form_data['probability'] = predict_proba.main(filename, test)
            clgData = CollegeData()
            form_data['college'] = clgData.get_college_name(form_data['college'])
            form_data['category'] = clgData.get_category_name(form_data['category'])
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            return render(request, 'index.html', {'form': form, 'form_data': form_data, 'flag': flag})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form, 'flag': flag})

def getBranches(request):
    college = request.GET.get('college')
    branches = pickle.load(open('myapp/data/pickles/branches.pkl','rb'))
    return HttpResponse(json.dumps(branches[college]))
    

def userPreference(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PredictCollege(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = flatten_to_dict(form)
            # collect college list according to the seleted criteria
            colleges = generate_list.generate(form_data['score'],form_data['branch'],form_data['category'],'myapp/data/pickles/')
            flag = True if len(colleges) != 0 else False
            clgData = CollegeData()
            form_data['branch'] = clgData.get_branch_name(form_data['branch'])
            form_data['category'] = clgData.get_category_name(form_data['category'])
            return render(request, 'smart_list.html', {'colleges':colleges, 'flag':flag, 'form_data':form_data})
    else:
        form = PredictCollege()
    return render(request, 'user_preference.html',{'form': form})

def smartList(request):
    fees = int(request.GET.get('selected_fees'))
    college_list = json.loads(request.GET.get('selected_colleges'))
    clgData = CollegeData()
    new_college_list = []
    for clg in college_list:
        if fees >= clgData.get_fees(clg[2]):
            new_college_list.append(clg)
    return HttpResponse(json.dumps(new_college_list))