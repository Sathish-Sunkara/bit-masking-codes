"""
same as unique number problem but here 2 unique numbers are there find them
"""
def find(arr):
    # find xor of all elements
    ans = 0
    for num in arr :
        ans ^= num

    bit = 1
    # find the right most set bit of answer
    while bit & ans == 0 :
        bit <<= 1

    #now split the array
    a = 0 ; b = 0
    for num in arr :
        if num & bit :
            a ^= num
        else :
            b ^= num
    return a , b


arr = [1,2,3,7,8,3,2,1]
print(find(arr))