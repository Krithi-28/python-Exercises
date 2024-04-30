import random
def quicksort(a):
    if  len(a)<=1:
        return a
    pivot=random.choice(a)
    left=[i for i in a if i<pivot]
    middle=[i for i in a if i==pivot]
    right=[i for i in a if i>pivot]
    return quicksort(left)+middle+quicksort(right)


a=list(map(int,input().split()))
print(quicksort(a))