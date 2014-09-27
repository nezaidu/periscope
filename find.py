from bisect import bisect_left
def find(a, x):
    'Locate the leftmost value exactly equal to x'
    if len(x)<=3:
    	return 1
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    if i != len(a) and a[i] == x+'\r':
        return i
    return 0