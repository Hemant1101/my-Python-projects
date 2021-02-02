# author:Hemant1101
# lang: Python3
# topic: arithmetical operations over list

# 1 sum of all elements:

l1=[1,2,3,4,5]
temp=0
for item in range(len(l1)):
    temp = temp+ l1[item]
print('Sum of all number in list is '+ str(temp))

# 2 product of all elements:

l1=[1,2,3,4,5]
temp=0
for item in range(len(l1)):
    if(temp==0):
        temp = temp + l1[item]
    else:
        temp=temp*l1[item]
print('multiple of all number in list is '+ str(temp))

# 3 max element in list

l1=[1,2,3,4,5]
max_num = l1[0]
for item in l1:
    if item > max_num:
        max_num = item
print('maximum value in list is '+str(max_num))

# 4 min element in list

l1=[1,2,3,4,5]
min_num = l1[0]
for item in l1:
    if item < min_num:
        max_num = item
print('minimum value in list is '+str(min_num))

