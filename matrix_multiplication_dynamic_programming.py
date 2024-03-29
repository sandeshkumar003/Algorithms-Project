import numpy as np
import random as rd

x=rd.randint(1,50)
n= rd.randint(1,50)
Papa_mat = []

m=[x]
for i in range(n):
    y=rd.randint(1,50)
    Matrix = np.random.randint(20, size=(x,y))
    print(x,y)
    Papa_mat.append(Matrix)
    x=y
    m.append(x)

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
print(MatrixChainOrder(m,n))


