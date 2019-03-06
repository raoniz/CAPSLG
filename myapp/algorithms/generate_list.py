import pickle
import numpy as np
from . import predict_proba

COLLEGE_CHOICES = {
    "vjti": "Veermata Jijabai Technological Institute",
    "sp": "Sardar Patel College of Engineering",
    "spit": "Bhartiya Vidya Bhavan's Sardar Patel Institute of Technology",
    "ict":"Institute of Chemical Technology",
    "kjsce":"K.J.Somaiya College of Engineering",
    "kjit":"K J Somaiya Institute of Engineering and Information Technology",
    "vik": "Vivekanand Education Society's Institute of Technology",
    "sa": "Mahavir Education Trust's Shah & Anchor Kutchhi Engineering College",
    "dbit":"Don Bosco Institute of Technology",
    "djs":"Dwarkadas J. Sanghvi College of Engineering(DJ)",
    "fcr":"Fr. Conceicao Rodrigues College of Engineering",
    "ss": "Anjuman-I-Islam's M.H. Saboo Siddik College of Engineering",
    "rgit": "Manjara Charitable Trust's Rajiv Gandhi Institute of Technology",
    "rcr": "Rizvi Education Society's Rizvi College of Engineering",
    "bvc":" Bharati Vidyapeeth College of Engineering",
    "dmc":"N.Y.S.S.'s Datta Meghe College of Engineering",
    "afrc":"Agnel Charities' FR. C. Rodrigues Institute of Technology",
    "kc": "K.C. College of Engineering and Management Studies and Research",
    "kgc": "Konkan Gyanpeeth College of Engineering",
    "ltc":"Lokmanya Tilak College of Engineering",
    "mgm":"M.G.M.'s College of Engineering and Technology",
    "pvp":"Padmabhushan Vasantdada Patil Pratishthans College of Engineering",
    "pit": "M.E.S Pillai's Institute of Information Technology, Engineering Media Studies and Research",
    "rait": "Ramrao Adik Edu Soc, Ramarao Adik Institute of Tech (RAIT)",
    "jc":"Shivajirao S. Jondhale College of Engineering",
    "sies":"S.I.E.S. Graduate School of Technology",
    "sfit":"St. Francis Institute of Technology",
    "tec": "Terna Engineering College",
    "tcet": "Thakur College of Engineering and Technology",
    "tse":"Thadomal Shahani Engineering College",
    "vit":"Vidyalankar Institute of Technology"
}

# all college list
urls = ["vjti","sp","spit","ict","kjsce","kjit","vik","sa","dbit","djs","fcr","ss","rgit","rcr","bvc","dmc","afrc","kc","kgc","ltc","mgm","pvp","pit","rait","jc","sies","sfit","tec","tcet","tse","vit"]

def generate(score,branch,category,path):
	selected_colleges = []
	for url in urls:
		# retrive branches for particular college
		branches = pickle.load(open(path + 'branches.pkl','rb'))
		id_branches = [x for x,_ in branches[url]]

		# if selected branch is in the list then predict result
		if branch in id_branches:
			test = np.array([2019, branch, category, score])
			if predict_proba.selected(path + 'colleges/' + url + '.pkl', test.copy()):
				probability = predict_proba.main(path + 'colleges/' + url + '.pkl', test.copy())
				combination = [COLLEGE_CHOICES[url],probability,url]
				selected_colleges.append(combination)

	
	
	# '{0:.2f}'.format(probability)
	selected_colleges = sorted(selected_colleges,key=lambda x: x[1],reverse=True)
	selected_colleges = [[x,'{0:.4f}'.format(y),z] for x,y,z in selected_colleges]
	return selected_colleges[0:15]

if __name__ == '__main__':
	print(generate(20,'Production','GOPEN','../data/pickles/'))

	