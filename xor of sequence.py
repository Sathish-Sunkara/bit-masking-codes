"""
this creates xor of numbers from [0,n] 
"""
# 0 ==> n
# 1 ==> 1
# 2 ==> n+1
# 3 ==> 0
def xor(n):
    if n%4 == 0 :
        return n 
    if n%4 == 1 :
        return 1
    if n%4 == 2 :
        return n + 1
    if n%4 == 3 :
        return 0
    
print(xor(444))