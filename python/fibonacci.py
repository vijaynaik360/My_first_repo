def fiba(n):
    if n<=0:
        return "Input should be a positive integer."
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fiba(n-1)+fiba(n-2)
    
print(fiba(5))