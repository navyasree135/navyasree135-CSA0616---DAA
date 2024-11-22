import math
def unique_element(m,n):
    return math.comb(m+n-2, m-1)
print(unique_element(7,3))
