n=10
C=[[0]*n]*n
m=[]
print(C)
for i in range(0, n): 
    C[i][i] = 0
for s in range (0, n - 1):
    for i in range(0 , n - s):
        j = i + s
        val=float("inf")
        for k in range(i-1,j):
            temp= min(C[i][k] + C[k + 1][j] +m[i-1]*m[k]*m[j])
            if temp <val:
                val=temp
        
C[1][n]