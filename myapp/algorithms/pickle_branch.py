import pickle

vjti = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Textile','Textile'),
)

sp = (
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('Mechanical','Mechanical'),
    
)

spit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    )

ict = (
    ('Chemical', 'Chemical'),
    ('DyestuffTechnology', 'Dyestuff Technology'),
    ('OleochemicalsandSurfactantsTechnology', 'Oleochemicals and Surfactants Technology'),
    ('PharmaceuticalsChemistryandTechnology', 'Pharmaceuticals Chemistry and Technology'),
    ('FibresandTextileProcessingTechnology','Fibres and Textile Processing Technology'),
    ('PolymerEngineeringandTechnology','Polymer Engineering and Technology'),
    ('SurfaceCoatingTechnology','Surface Coating Technology'),
)

kjsce = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),    
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),
)

kjit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
)

vik = (    
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Instrumental','Instrumental'),
)

sa = (    
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
)

dbit = (    
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('Mechanical','Mechanical'),
)

djs = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),    
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production '),
    ('Mechanical','Mechanical'),
    ('BioMedical','Bio Medical'),
)

fcr = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('ETRX','ETRX'),
    ('Production','Production'),
)

ss = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Automobile','Automobile'),
    ('Mechanical','Mechanical'),    
)

rgit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('Instrumental','Instrumental'),
    ('Mechanical','Mechanical'),   
)

rcr = (
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('ETRX', 'ETRX'),
    ('EXTC','EXTC'),
    ('BioTechnology','Bio Technology'),
    ('Mechanical','Mechanical'),
)

bvc = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('Mechanical','Mechanical'),
    ('Instrumentation','Instrumentation'),
)

dmc = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),
    )

afrc = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('Mechanical','Mechanical'),
)

kc = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
)

kgc = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Instrumentation','Instrumentation'),
)

ltc = (
    ('Computer', 'Computer Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),    
)

mgm = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('BioTechnology','Bio Technology'),
    ('Mechanical','Mechanical'),
    ('BioMedical','Bio Medical'),
)

pvp = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    )

pit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),
    ('Automobile','Automobile'),
)

rait = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Instrumentation','Instrumentation'),
)

jc = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
   )

sies = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('PrintingandPacking','Printing and Packing'),
    ('Mechanical','Mechanical'),
    )

sfit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    )

tec = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),
    ('Mechatronics','Mechatronics'),
)

tcet = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Mechanical','Mechanical'),
    )

tse = (
    ('Chemical', 'Chemical'),
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('EXTC','EXTC'),
    ('BioMedical','Bio Medical'),
    ('BioTechnology','Bio Technology'),
)

vit = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('BioMedical','Bio Medical'),
)

branches = {'vjti':vjti,'sp':sp,'spit':spit,'ict':ict,'kjsce':kjsce,'kjit':kjit,'vik':vik,'sa':sa,'dbit':dbit,'djs':djs,'fcr':fcr,'ss':ss,'rgit':rgit,'rcr':rcr,'bvc':bvc,'dmc':dmc,'afrc':afrc,'kc':kc,'kgc':kgc,'ltc':ltc,'mgm':mgm,'pvp':pvp,'pit':pit,'rait':rait,'jc':jc,'sies':sies,'sfit':sfit,'tec':tec,'tcet':tcet,'tse':tse,'vit':vit}

with open("../data/pickles/branches.pkl",'wb') as file:
	pickle.dump(branches,file)