"""
given array all numberrs are repetaed twice one number is repeated only once find that number
"""
def find(arr):
    ans = 0
    for num in arr :
        ans ^= num
    return ans 

arr = [1,2,3,2,5,1,3]  # apply for unique number finding
arr = [1,1,2,2,2,2,3,3,3]  # finding odd number of repeated items,other are repeated even times
print(find(arr))

