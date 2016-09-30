#main code for extracting the information, and formatting it. 
import csv

from sklearn import datasets, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
from sklearn import ensemble

import numpy as np


data = []
personal = {}

with open('voterfileNym.csv', newline='') as csvfile:
    data_csv = csv.reader(csvfile)
    for row in data_csv:
        data.append(row)

for i in range (0, len(data)):
    personal[data[i][0]] = [x for x in data[i]]
    personal[data[i][0]].pop(0)

numlist = []
targets = []

for key in personal.keys():
    numlist.append([personal[key][x] for x in range(0, len(personal[key])-1)])
    summation = 0
    for i in range(10, 25):
        summation += int(personal[key][i])
    average = summation/14
    targets.append(average)

npNumlist = np.array(numlist).astype(np.float)
npTargets = np.array(targets).astype(np.float)


model = linear_model.LogisticRegression()
model.fit(npNumlist, npTargets) #fit training data          

expected = npTargets
predicted = model.predict_proba(npNumlist)

counter = 0
for key in personal.keys():
    personal[key].insert(0,key)
    personal[key].append("%.3f" % predicted[counter][1])
    if(predicted[counter][1] >= 0.5):
        personal[key].append('1')
    else:
        personal[key].append('0')     
    counter += 1