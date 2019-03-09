import pickle
import numpy as np
from . import predict_proba
from .. models import CollegeData
import googlemaps

# all college list
urls = ["vjti","sp","spit","ict","kjsce","kjit","vik","sa","dbit","djs","fcr","ss","rgit","rcr","bvc","dmc","afrc","kc","kgc","ltc","mgm","pvp","pit","rait","jc","sies","sfit","tec","tcet","tse","vit"]

def generate(score,branch,category,location,path):
	selected_colleges = []
	origin_loc = CollegeData.get_lat_lng(location)
	for url in urls:
		# retrive branches for particular college
		branches = pickle.load(open(path + 'branches.pkl','rb'))
		id_branches = [x for x,_ in branches[url]]

		# if selected branch is in the list then predict result
		if branch in id_branches:
			test = np.array([2019, branch, category, score])
			if predict_proba.selected(path + 'colleges/' + url + '.pkl', test.copy()):
				probability = '{0:.4f}'.format(predict_proba.main(path + 'colleges/' + url + '.pkl', test.copy()))
				distance, duration = CollegeData.get_dist_dur(url, origin_loc)
				# distance, duration = 0,0
				combination = [CollegeData.get_college_name(url),
                                probability,
                                CollegeData.get_fees(url),
                                CollegeData.get_grade(url),
                                CollegeData.get_location_name(url),
                                distance,
                                duration,
                                url]
				selected_colleges.append(combination)
	
	# '{0:.2f}'.format(probability)
	selected_colleges = sorted(selected_colleges,key=lambda x: x[1],reverse=True)
	return selected_colleges[0:15]

if __name__ == '__main__':
	print(generate(20,'Production','GOPEN','../data/pickles/'))

	