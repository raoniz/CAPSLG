from sklearn import preprocessing
import pickle

def main():
    le = preprocessing.LabelEncoder()
    category = ['GOBC', 'GOPEN', 'LOBCS', 'LOPEN', 'PWDC']
    branches = ['Chemical','IT','Computer','Civil','Electrical','EXTC','ETRX','Production','Mechanical','Textile','DyestuffTechnology','OleochemicalsandSurfactantsTechnology','PharmaceuticalsChemistryandTechnology','FibresandTextileProcessingTechnology','PolymerEngineeringandTechnology','SurfaceCoatingTechnology','Instrumental','BioMedical','Automobile','Instrumentation','BioTechnology','PrintingandPacking','Mechatronics']
    branches.extend(category)
    le.fit(branches)

    filename = '../data/pickles/label_fit.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(le, f)

if __name__ == '__main__':
    main()
