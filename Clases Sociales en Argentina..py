# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EEc4cluYNgzGlUi2dfp_P_ZaLud7TfaE
"""

import pandas as pd

datos = pd.read_csv('clasesArgentinas.csv')

datos

caracteristicas =[90000,121000,251000, 45100]

etiquetas =[0,1,2,3]

from sklearn import tree

clasificador= tree.DecisionTreeClassifier()

clasificador.fit(caracteristicas,etiquetas)

prediccion=clasificador.predict([100000])
ingresos1 = int (input("ingresar monto minimo: "))

prediccion = clasificador.predict([[ingresos1]])

if (prediccion ==0):
  print ("la clase es superior baja")
if (prediccion ==1):
    print ("la clase es media baja")
if (prediccion ==2):
  print ("la clase es media alta")
else:
  print ("la clase es media alta")