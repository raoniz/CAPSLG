from django.db import models
from django import forms

# Create your models here.
CATEGORY_CHOICES = (
    ('GOPEN', 'General Open'),
    ('GOBC','General Other Backward Class(OBC)'),
    ('PWDC','Persons with Disabilities'),
    ('LOPEN', 'Ladies Open'),
    ('LOBCS', 'Ladies Other Backward Class(OBC)'),
)

INITIAL_BRANCH_CHOICES = (
    ('IT', 'Information Techonology'),
    ('Chemical', 'Chemical'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Textile','Textile'),
)

BRANCH_CHOICES = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Chemical', 'Chemical'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Textile','Textile'),
    ('DyestuffTechnology', 'Dyestuff Technology'),
    ('OleochemicalsandSurfactantsTechnology', 'Oleochemicals and Surfactants Technology'),
    ('PharmaceuticalsChemistryandTechnology', 'Pharmaceuticals Chemistry and Technology'),
    ('FibresandTextileProcessingTechnology','Fibres and Textile Processing Technology'),
    ('PolymerEngineeringandTechnology','Polymer Engineering and Technology'),
    ('SurfaceCoatingTechnology','Surface Coating Technology'),
    ('Instrumental','Instrumental'),
    ('BioMedical','Bio Medical'),
    ('Automobile','Automobile'),
    ('Instrumentation','Instrumentation'),
    ('BioTechnology','Bio Technology'),
    ('PrintingandPacking','Printing and Packing'),
    ('Mechatronics','Mechatronics'),
)

COLLEGE_CHOICES = (
    ("vjti", "Veermata Jijabai Technological Institute"),
    ("sp", "Sardar Patel College of Engineering"),
    ("spit", "Bhartiya Vidya Bhavan's Sardar Patel Institute of Technology"),
    ("ict","Institute of Chemical Technology"),
    ("kjsce","K.J.Somaiya College of Engineering"),
    ("kjit","K J Somaiya Institute of Engineering and Information Technology"),
    ("vik", "Vivekanand Education Society's Institute of Technology"),
    ("sa", "Mahavir Education Trust's Shah & Anchor Kutchhi Engineering College"),
    ("dbit","Don Bosco Institute of Technology"),
    ("djs","Dwarkadas J. Sanghvi College of Engineering(DJ)"),
    ("fcr","Fr. Conceicao Rodrigues College of Engineering"),
    ("ss", "Anjuman-I-Islam's M.H. Saboo Siddik College of Engineering"),
    ("rgit", "Manjara Charitable Trust's Rajiv Gandhi Institute of Technology"),
    ("rcr", "Rizvi Education Society's Rizvi College of Engineering"),
    ("bvc"," Bharati Vidyapeeth College of Engineering"),
    ("dmc","N.Y.S.S.'s Datta Meghe College of Engineering"),
    ("afrc","Agnel Charities' FR. C. Rodrigues Institute of Technology"),
    ("kc", "K.C. College of Engineering and Management Studies and Research"),
    ("kgc", "Konkan Gyanpeeth College of Engineering"),
    ("ltc","Lokmanya Tilak College of Engineering"),
    ("mgm","M.G.M.'s College of Engineering and Technology"),
    ("pvp","Padmabhushan Vasantdada Patil Pratishthans College of Engineering"),
    ("pit", "M.E.S Pillai's Institute of Information Technology, Engineering Media Studies and Research"),
    ("rait", "(RAIT)Ramrao Adik Edu Soc, Ramarao Adik Institute of Tech"),
    ("jc","Shivajirao S. Jondhale College of Engineering"),
    ("sies","S.I.E.S. Graduate School of Technology"),
    ("sfit","St. Francis Institute of Technology"),
    ("tec", "Terna Engineering College"),
    ("tcet", "Thakur College of Engineering and Technology"),
    ("tse","Thadomal Shahani Engineering College"),
    ("vit","Vidyalankar Institute of Technology"),
)

FEES = {'vjti':83805,
        'sp':85020,
        'spit':149000,
        'ict':81000,
        'kjsce':173680,
        'kjit':132605,
        'vik':107790,
        'sa':108000,
        'dbit':122770,
        'djs':134750,
        'fcr':145085,
        'ss':118890,
        'rgit':96470,
        'rcr':82000,
        'bvc':85750,
        'dmc':92500,
        'afrc':140000,
        'kc':130000,
        'kgc':99000,
        'lti':117856,
        'mgm':82500,
        'pvp':122960,
        'pit':117000,
        'rait':88000,
        'jc':86000,
        'sies':105500,
        'sfit':108210,
        'tec':90250,
        'tcet':121500,
        'tse':142500,
        'vit':136272
    }

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=15, widget=forms.Select(choices=CATEGORY_CHOICES))
    score = forms.IntegerField()
    college = forms.CharField(max_length=15, widget=forms.Select(choices=COLLEGE_CHOICES))
    # branch = forms.CharField(max_length=15, widget=forms.Select(choices=BRANCH_CHOICES))
    branch = forms.ChoiceField(choices=INITIAL_BRANCH_CHOICES)

class PredictCollege(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=15, widget=forms.Select(choices=CATEGORY_CHOICES))
    score = forms.IntegerField()
    branch = forms.ChoiceField(choices=BRANCH_CHOICES)

class CollegeData(models.Model):
    fees = FEES