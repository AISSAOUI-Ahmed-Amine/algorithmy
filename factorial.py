def factor(p):
    if p == 0:
        return 1
    else :
        return p*factor(p-1)

test = factor(3)
print(test)