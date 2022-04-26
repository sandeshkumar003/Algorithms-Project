import numpy as np
import random as rd
from matplotlib import pyplot as plt
import timeit

#Analysis for brute force and strassen
'''
def bruteforce(mat_A,mat_B,n):
    mat_C = [[0 for y in range (n)] for x in range (n)]

    for i in range (n):
        for j in range (n):
            mat_C[i][j] = 0
            for k in range (n):
                mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
    return mat_C
def visualization(n):    
    x_values=[]
    listBrute=[]
    listStrassen=[]
    for i in range(1,n):
        x_values.append(i)
        mat_A = np.random.randint(20, size=(n,n))
        mat_B = np.random.randint (20, size=(n,n))
        #Brute Force
        start=time.time()
        mat_C =bruteforce(mat_A,mat_B,n)
        end=time.time()
        listBrute.append(end-start)
    
visualization(50)
'''
'''
mat_A = np.random.randint(50, size=(50,50))
# print(mat_A,"mata", len(mat_A))
mat_B = np.random.randint (50, size=(50,50))
# print(mat_B,'matb', len(mat_B))
'''

def split(mat):
    r, c = mat.shape
    r_1, c_1 = r//2, c//2
    return mat[:r_1, :c_1], mat[:r_1, c_1:], mat[r_1:, :c_1], mat[r_1:, c_1:]

def strassen(x, y):
    if x.shape[0] == 1:
        return x * y
        
    else:
        mat_A_q1, mat_A_q2, mat_A_q3, mat_A_q4 = split(x)
        mat_B_q1, mat_B_q2, mat_B_q3, mat_B_q4 = split(y)

        prod_1 = strassen(mat_A_q1, mat_B_q2 - mat_B_q4)
        prod_2 = strassen(mat_A_q1 + mat_A_q2, mat_B_q4)
        prod_3 = strassen(mat_A_q3 + mat_A_q4, mat_B_q1)
        prod_4 = strassen(mat_A_q4, mat_B_q3 - mat_B_q1)
        prod_5 = strassen(mat_A_q1 + mat_A_q4, mat_B_q1 + mat_B_q4)
        prod_6 = strassen(mat_A_q2 - mat_A_q4, mat_B_q3 + mat_B_q4)
        prod_7 = strassen(mat_A_q1 - mat_A_q3, mat_B_q1 + mat_B_q2)
        
        mat_c_q1 = prod_5 + prod_4 - prod_2 + prod_6
        mat_c_q2 = prod_1 + prod_2
        mat_c_q3 = prod_3 + prod_4
        mat_c_q4 = prod_1 + prod_5 - prod_3 - prod_7
        
        mat_C = np.vstack((np.hstack((mat_c_q1, mat_c_q2)), np.hstack((mat_c_q3, mat_c_q4))))
        return mat_C

# result = strassen(mat_A, mat_B)
# print(result)
# print(len(result))
def bruteforce(mat_A,mat_B,n):
    mat_E = [[0 for y in range (n)] for x in range (n)]

    for i in range (n):
        for j in range (n):
            mat_E[i][j] = 0
            for k in range (n):
                mat_E[i][j] += mat_A[i][k] * mat_B[k][j]
           
    return mat_E

def visualization(n):    
    x_values=[]
    listBrute=[]
    listStrassen=[]
    for i in range(1,n):
        ith=2**i
        x_values.append(2**i)
        mat_A = np.random.randint(20, size=(ith,ith))
        mat_B = np.random.randint (20, size=(ith,ith))
        
        
        #Brute Force
        start=timeit.default_timer()
        mat_E = bruteforce(mat_A,mat_B,ith)
        end=timeit.default_timer()
        listBrute.append(end-start)
        start1 = timeit.default_timer()
        mat_C =strassen(mat_A,mat_B)
        end1 = timeit.default_timer()
        listStrassen.append(end1-start1)
        print(end1,start1)
        
        mat_A=mat_A.tolist()
        mat_B=mat_B.tolist()
        print(type(mat_A),type(mat_B))
    print(x_values,listStrassen)
    print(x_values,listBrute)
    plt.plot(x_values,listBrute,label="Brute Force")
    plt.plot(x_values,listStrassen,label="Strassen")
    plt.legend()
    plt.show()
visualization(3)
