"""
to add 2 numbers without + 
"""
def add(a , b) :

    ans = 0
    carry = 0
    pos = 0
    while ((a != 0) or (b != 0)) :
        one = 0
        one += a&1
        one += b&1
        one +=  carry
        carry = one // 2
        if (one % 2) :
            ans = ans ^ (1<<pos)
        a = a >> 1
        b = b >> 1
        pos += 1
    if carry == 1 :
        ans = ans ^ (1 << pos)

    return ans


a = 5
b = 5
print(add(a,b))