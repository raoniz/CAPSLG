import pickle
import numpy as np

def main(filename, test):
    le = pickle.load(open('../data/pickles/label_fit.pkl', 'rb'))
    test[1:3] = le.transform(test[1:3])
    test = test.reshape(1,-1)

    newmodel = pickle.load(open(filename, 'rb'))
    newmodel.predict(test)
    # print('AdaBoost Score: ', newmodel.score(test, test_labels))
    return newmodel.predict_proba(test)[0][1] * 100

if __name__ == '__main__':
    print(main('../data/pickle/vjti.pkl', np.array(input('Enter test data: ').strip().split(' '))))
