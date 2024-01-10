
 #return number ones in binary number string
#n  1 discard the last digit and value by n2 
# count as n & 1 will gives last one is 1 or not

def counts1(n) :
    # normal 0(n)
    count = 0
    for ch in str(bin(n)[2:]) :
        if ch == "1" :
            count += 1
    return count

def counts2(n):
    count = 0
    while n > 0 :
        n = n&(n-1)
        count += 1
    return count

def counts3(n) :
    count = 0
    while n > 0 : 
        count += int(n&1)
        n = n >> 1
    return count



n = 1024

print(counts1(n))
print(counts2(n))
print(counts3(n))

