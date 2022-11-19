def integer11(a):
    a1=a%10
    a2=int(a/10)%10
    a3=int(a/100)%10
    return a1+a2+a3, a1*a2*a3
print(integer11(497))
