# -*- coding: utf-8 -*-
"""
@author: Murilo Spina
"""

from sklearn import tree
#from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import numpy as np

X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37],
     [166,65,40], [190,90,47], [175,64,39], [177,70,40],
     [159,55,37], [171,75,42], [181,85,43]]
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
     'male', 'female', 'male', 'female', 'male']

#classificadores
classificador_tree = tree.DecisionTreeClassifier()
classificador_KNN = KNeighborsClassifier()
classificador_perc = Perceptron()
classificador_gau = GaussianNB()

#Treinando classificadores
classificador_tree = classificador_tree.fit(X,Y)
classificador_KNN = classificador_KNN.fit(X, Y)
classificador_perc = classificador_perc.fit(X, Y)
classificador_gau = classificador_gau.fit(X,Y)

#teste Arvore de decisão
prediction_tree = classificador_tree.predict(X)
accuracy_tree = accuracy_score(Y, prediction_tree) * 100

#teste KNN
prediction_KNN = classificador_KNN.predict(X)
accuracy_KNN = accuracy_score(Y, prediction_KNN) * 100

#Teste Perceptron
prediction_perc = classificador_perc.predict(X)
accuracy_perc = accuracy_score(Y, prediction_perc) * 100

#Teste Gaussian
prediction_gau = classificador_gau.predict(X)
accuracy_gau = accuracy_score(Y, prediction_perc) * 100

if accuracy_tree > accuracy_KNN:
    print('Método Árvore de Decisão é mais preciso com {}%'.format(accuracy_tree))
elif accuracy_KNN > accuracy_perc:
    print('Método KNN é mais preciso com {}%'.format(accuracy_KNN))
elif accuracy_perc > accuracy_gau:
    print('Método Perceptron é mais preciso com {}%'.format(accuracy_perc))
elif accuracy_gau > accuracy_tree:
    print('Método GaussianNB é mais preciso com {}%'.format(accuracy_gau))
    

print('Precisão para DecisionTree: {}%'.format(accuracy_tree))
print('Precisão para KNN:  {}%'.format(accuracy_KNN))
print('Precisão para Perceptron:  {}%'.format(accuracy_perc))
print('Precisão para GaussianNB:  {}%'.format(accuracy_gau))



