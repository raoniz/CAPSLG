import random as rn
import pandas
import numpy as np

# constants
path_retrieve = "../data/raw_data/"
path_store = "../data/train_data/"
names = ['Year', 'Branch', 'Category', 'Score']
max_score = 200

urls = ["vjti","sp","spit","ict","kjsce","kjit","vik","sa","dbit","djs","fcr","ss","rgit","rcr","bvc","dmc","afrc","kc","kgc","ltc","mgm","pvp","pit","rait","jc","sies","sfit","tec","tcet","tse","vit"]

for url in urls:
    dataframe = pandas.read_csv(path_retrieve + url + ".csv", names=names)
    array = dataframe.values
##    array = array[20:21]

    newArray = []
    for row in array:
        
        score = row[len(row)-1]
        if(score != 0):
            below_score = rn.sample(population=range(score), k=5)
        else:
            below_score = rn.sample(population=range(score,max_score), k=5)
        above_score = rn.sample(population=range(score,max_score), k=4)
        above_score.append(score)
        above_score.extend(below_score)

        new_row = []
        for i in range(len(row)-1):
            new_row.append(row[i])
        new_row.extend(range(0,2));

        for i in above_score:
            new_row[3] = i
            if score == 0:
                new_row[4] = 0
            elif i < score:
                new_row[4] = 0
            else:
                new_row[4] = 1
            newArray.append(new_row.copy())

    print(url, len(newArray))
    

    array = np.array(newArray)
    pandas.DataFrame(array).to_csv(path_store + url + ".csv", header=None, index=None)
