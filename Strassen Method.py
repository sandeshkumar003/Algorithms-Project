import numpy as np

mat_A = np.random.randint(20, size=(128,128))
mat_B = np.random.randint (20, size=(128,128))

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

print(strassen(mat_A, mat_B))