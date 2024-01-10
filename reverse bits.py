"""
reverse the bits in a number and return that numbe
"""

def reverse(n):
    if n == 0 :
        return 0
    res = 0
    while n > 0 :
        res = res << 1 
        if n & 1 == 1 :
            res += 1
        n  = n >> 1
    return res

n = 22
print(reverse(n))
print(bin(reverse(n)))

