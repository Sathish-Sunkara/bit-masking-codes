def set_zero(n):
    #sets the last set bit to 0
    return n & (n-1)

def find_ith_bit(n,i):
    # finds the bit in ith position
    n = n & (1<<i)
    if n == (1<<i) :
        return 1
    else: # here condition to get 0 is "n == 0"
        return 0

def set_ith_one(n,i):
    # sets the ith from last to 1 if there already a 1 then no change
    n = n | (1<<i)
    return n
def set_ith_zero(n,i):
    # at index i from last , sets that bit to zero if one is present 
    n = n & (~(1<<i))
    return n

def complement_ith(n,i):
    # it complements the ith bit in number "it takes help from function " find_ith_bit() " "
    bit = find_ith_bit(n,i) # finds bit at ith position
    if bit == 1 : # if its one set to zero 
        return set_ith_zero(n,i)
    else:
        return set_ith_one(n,i)
def get_LSB(n):
    return n&1


    


n =21 
i = 3
print(complement_ith(n, i ))