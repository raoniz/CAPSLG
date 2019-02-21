import pandas
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

# Change as per the name and location of the training data file
def main(data_url, pickle_name):
    url = '../data/train_data/'
    url += data_url

    names = ['Year', 'Branch', 'Category', 'Score', 'Admission']
    dataframe = pandas.read_csv(url, names=names)
    array = dataframe.values
    le = pickle.load(open('../data/pickles/label_fit.pkl', 'rb'))
    for i in range(1,3):
        array[:,i] = le.transform(array[:,i])

    # print(array)
    # array = array.astype('int')
    X = array[:,0:4]
    Y = array[:,4].astype(int)
    seed = 7
    num_trees = 40

    train, test, train_labels, test_labels = train_test_split(X, Y, test_size=0.3,  random_state=seed)

    adamodel = AdaBoostClassifier(DecisionTreeClassifier(max_depth=5),
                             algorithm="SAMME",n_estimators=num_trees, random_state=seed)
    adamodel.fit(train, train_labels)

    # Store with respective college name
    filename = '../data/pickles/'
    filename += pickle_name

    with open(filename, 'wb') as f:
        pickle.dump(adamodel, f)

if __name__ == '__main__':
    main('vjti.csv', 'vjti.pkl')
