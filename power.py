def power(x,n):
    if x == 0 and n==0:
        print("Error")
        
    elif x == 0 and n != 0:
        return 0
    
    elif n == 0 or x == 1:
        return 1
    
    elif n == 1 :
        return x
    
    else :
        return x*power(x, n-1)


test = power(2, 3)
print(test)