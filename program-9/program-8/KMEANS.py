# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:57:19 2018

@author: sharmila
"""

import csv

#import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

#1.Load Data
def loadCsv(filename):
	lines = csv.reader(open(filename, "rt"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

filename = "sample_stocks.csv"
X = loadCsv(filename)
print(X)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

colors = ["g.","r.","y."]

for i in range(len(X)):
    #print("coordinate:",X[i],"label:",labels[i])
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize = 20)
    
plt.scatter(centroids[:,0],centroids[:,1] ,marker = 'x', s=100,linewidth = 2,zorder=10)
plt.show()

