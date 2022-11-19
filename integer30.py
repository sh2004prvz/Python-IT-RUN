def int30(x):
    if x%10 == 0:
        return x//100
    else:
        return x//100+1
print(int30(101))