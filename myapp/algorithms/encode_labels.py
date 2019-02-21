from sklearn import preprocessing
import pickle

def main():
    le = preprocessing.LabelEncoder()
    le.fit(['Civil', 'Computer', 'IT', 'GOBC', 'GOPEN', 'LOBCS', 'LOPEN', 'PWDC'])

    filename = '../data/pickles/label_fit.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(le, f)

if __name__ == '__main__':
    main()
