from turtle import width
import numpy as np
import random as rd
from matplotlib import pyplot as plt
import time

#Analysis for brute force and strassen

def bruteForce(mats):
    n= len(mats)
    n_steps=[]
    total=0
    #genrating random numbers
    for i in mats:
        n_steps.append(len(i))
    n_steps.append(len(i[0]))   
    for i in range(2,len(n_steps)):
        total+=n_steps[i]*n_steps[i-1]*n_steps[0]
    return total

def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
    return m[1][n-1]
def visualization(n):    
    x_values=[]
    listBrute=[]
    mats=[]
    listChain=[]
    for i in range(3,n):
        x=rd.randint(1,50)
        m=[x]
        x_values.append(i)
        for j in range(i):
            y=rd.randint(1,50)
            matriks=np.random.randint(20, size=(x,y))
            mats.append(matriks)
            x=y
            m.append(y)
        multiplications =bruteForce(mats)
        listBrute.append(multiplications)
        multiplications=MatrixChainOrder(m,i)
        listChain.append(multiplications)
    print(listBrute)
    print(listChain)
    for i in range(len(x_values)):
        x_values[i]-=0.1
    plt.bar(x_values,listBrute, width=0.2, color="green",
                label="Brute Force", align="center")
    for i in range(len(x_values)):
        x_values[i]+=0.2
    plt.bar(x_values,listChain, width=0.2,color="red",
                label="Matrix Chain Mutiplication", align="center")
    plt.show()
visualization(10)