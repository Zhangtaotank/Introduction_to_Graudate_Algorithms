def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(40))

# method2
def fibonacci2(n):solutions
    f = []
    f.append(0)
    f.append(1)
    if n >=2:
        for i in range(2,n+1):
            f.append(f[i-1] + f[i-2])
    return f[n]

print(fibonacci2(40))
