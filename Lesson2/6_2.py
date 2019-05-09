# hotel problem A1, A2, A3, A4,...An
# 1 subproblem: p(i) minimum penalty with the ending stop Ai  
def hotel(lis):
    P = [] 
    P.append(0) # the starting point the penalty is 0
    
    for i in range(1, len(lis)):
        P[i] = min([P[j] + (200-(lis[j]-lis[i]))**2 for j in range(0, i)])
        # for j in range(0, i):
            # pi = P[j] + (200-(lis[i]-lis[j]))**2
            # P_lis.append(pi)
        # print(P_lis)
        # minimum_p = min(P_lis)
        
        # P.append(minimum_p)
        
    return P 
    
lis = [201, 401,500, 700, 800, 801]

print(hotel(lis))