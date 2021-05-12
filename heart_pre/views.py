from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
def home(request):
    return render(request,'home.html')

def resultt(request):

    df= pd.read_csv('data.csv')
    X=df.drop(columns='target',axis=1)
    y=df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    logre = LogisticRegression()
    logre.fit(X_train,y_train)
    
    val1 = (request.GET['1'])
    val2 = (request.GET['2'])
    val3 = (request.GET['3'])
    val4 = (request.GET['4'])
    val5 = (request.GET['5'])
    val6 = (request.GET['6'])
    val7 = (request.GET['7'])
    val8 = (request.GET['8'])
    val9 = (request.GET['9'])
    val10 = (request.GET['10'])
    val11 = (request.GET['11'])
    val12 = (request.GET['12'])
    val13 = (request.GET['13'])


    lst = []
    lst.append(val1)
    lst.append(val2)
    lst.append(val3)
    lst.append(val4)
    lst.append(val5)
    lst.append(val6)
    lst.append(val7)
    lst.append(val8)
    lst.append(val9)
    lst.append(val10)
    lst.append(val11)
    lst.append(val12)
    lst.append(val13)

    in1 = np.asarray(lst)
    in2 = in1.reshape(1,-1)

    psd = logre.predict([lst])
    res=""

    if(psd[0]==0):
        res="Safe"
    else:
        res="Danger"
    
    
    return render(request,'result.html',{"result2":res})

