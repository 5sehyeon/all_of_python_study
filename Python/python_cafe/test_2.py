import re

def is_even(N):
    if N%2 == 0:
        return N

lst = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(is_even,lst)
print(list(even_number))
