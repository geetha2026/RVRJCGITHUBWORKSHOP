def nfactorial(n):
    f=1
    while n>1:
        f=f+n
    n=n-1
    return f   

print(nfactorial(10))
