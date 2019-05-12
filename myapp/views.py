from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rebar.testing import flatten_to_dict
from .algorithms import predict_proba, generate_list
import numpy as np
import pickle
import googlemaps
import json

from .models import UserForm, PredictCollege, CollegeData, ExportPdf

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
            branches_code = [x for x,_ in CollegeData.get_branch(form_data['college'])]
            probability = {}
            branches = []
            for b in branches_code:
                test = np.array([2019, b, form_data['category'], form_data['score']])
                b_name = CollegeData.get_branch_name(b)
                branches.append(b_name)
                probability[b_name] = predict_proba.main(filename, test)
            form_data['probability'] = probability
            form_data['branch'] = branches
            form_data['college'] = CollegeData.get_college_name(form_data['college'])
            form_data['category'] = CollegeData.get_category_name(form_data['category'])
            # redirect to a new URL:
            # return HttpResponseRedirect('/index/')
            return render(request, 'index.html', {'form': form, 'form_data': form_data, 'flag': flag})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form, 'flag': flag})

# def getBranches(request):
#     college = request.GET.get('college')
#     return HttpResponse(json.dumps(CollegeData.get_branch(college)))


def userPreference(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PredictCollege(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = flatten_to_dict(form)
            # collect college list according to the seleted criteria
            colleges = generate_list.generate(form_data['score'],form_data['branch'],form_data['category'],form_data['location'],'myapp/data/pickles/')
            flag = True if len(colleges) != 0 else False

            form_data['branch'] = CollegeData.get_branch_name(form_data['branch'])
            form_data['category'] = CollegeData.get_category_name(form_data['category'])
            return render(request, 'smart_list.html', {'colleges':colleges, 'flag':flag, 'form_data':form_data})
    else:
        form = PredictCollege()
    return render(request, 'user_preference.html',{'form': form})

def smartList(request):
    fees = int(request.GET.get('selected_fees'))
    college_list = json.loads(request.GET.get('selected_colleges'))
    distance = int(request.GET.get('selected_distance'))
    grade = int(request.GET.get('selected_grade'))
    # origin_loc = CollegeData.get_lat_lng(query);

    new_college_list = []
    for clg in college_list:
        coll_fees = CollegeData.get_fees(clg[7])
        coll_dist = clg[5]
        coll_grade = CollegeData.get_grade(clg[7])
        if coll_fees <= fees and coll_dist <= distance and coll_grade >= grade:
            new_college_list.append(clg)
    return HttpResponse(json.dumps(new_college_list))

def export_pdf(request):
    colleges = json.loads(request.GET.get('selected_colleges'))
    form_data = json.loads(request.GET.get('form_data'))
    flag = True if len(colleges) != 0 else False
    pdf, response = ExportPdf.export(colleges,form_data,flag)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
