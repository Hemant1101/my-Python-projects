# author:Hemant1101
# lang:  Python
# topic: list comprehensions

l: [int] = list(x for x in range(1, 11))     # list:[type] = list(expression for item in iterable)
print(l)
n = [x for x in range(1, 11)]                # list = [expression for item in iterable]
print(n)
m = [x for x in range(1, 20) if(x%2==0)]      # list:[type] = list(expression for item in iterable if condition)
print(m)
a = [x if x % 3 == 0 else -1 for x in range(1, 20)]  # list:[type]=list(expression if stmt else stmt for i in iterable)
print(a)

coordinates = [[x,y,z] for x in range(4) for y in range(4) for z in range(4) if((x+y+z)<4)]
print(coordinates)
x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if ((i + j + k) != n)]
print(l)
