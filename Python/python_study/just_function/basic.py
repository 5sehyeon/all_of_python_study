# filter 함수
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))

# map 함수
def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))

# lambda 함수(일회용 함수)
add = lambda x, y : x + y
print(add(3,5))
print(list(map(lambda x : x+2, [1,2,3,4,5])))

# 리스트 컴프리헨션
a = [x for x in range(10) if x > 5 ]
print(a)

# enumerate (행을 늘려가면서, 값을 차례대로 넣을 때)
lst = ["오세현","곽주원","김경민","우영우"]

for index, value in enumerate(lst):
    print(f"cell행은 {index+1}행, {index+1}행의 값은 {value}")



    
