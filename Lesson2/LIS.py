# this is a Longest Increasing Sequence problem

def lcs(x, y):
    L = [[0]*len(x) for k in range(len(y))] 
    
    for i in range(0, len(x)):
        L[i][0] = 0
    for j in range(0, len(y)):
        L[0][j] = 0
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1],L[i-1][j])
    return L[len(x)-1][len(y)-1]

    
l1 = "BCDBCDA"
l2 = "ABECBAA"

print(lcs(l1, l2))