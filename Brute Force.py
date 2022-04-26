import numpy as np

mat_A = np.random.randint(20, size=(128,128))
mat_B = np.random.randint (20, size=(128,128))
n = 128

mat_C = [[0 for y in range (n)] for x in range (n)]

for i in range (n):
    for j in range (n):
        mat_C[i][j] = 0
        for k in range (n):
            mat_C[i][j] += mat_A[i][k] * mat_B[k][j]

print(mat_C)