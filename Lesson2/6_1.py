def sumlis(lis):
    L = []
    
    L.append(lis[0]) # L[1] = a1
    
    for i in range(1, len(lis)):
        L.append(lis[i] + max(0, L[i-1]))
        
    return L
    
lis = [-1,-3,-5,6,3,-5,7]
print(sumlis(lis))

# This is another change.
    