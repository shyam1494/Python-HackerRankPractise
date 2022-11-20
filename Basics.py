# If-Else Condition

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    cond1 = range(2,5)
    cond2 = range(6,20)
    if(n%2 !=0):
        print('Weird')
    elif(n%2 ==0 and n in cond1 ):
        print('Not Weird')
    elif(n%2 ==0 and n in cond2):
        print("Weird")
    elif(n%2==0 and n > 20):
        print('Not Weird')
    else:
        print('Weird')
        
#list comprehension
if __name__ == '__main__':
    n = int(input())
    lst_comprehension = [x**2 for x in range(0,n)]
    for i in lst_comprehension:
        print(i)

#Unpacking the values:
if __name__ == '__main__':
    n = int(input())
    int_list = [x for x in range(1,n+1)]
    print(*int_list,sep='')

#Finding the minimum and maximum in array :

import numpy as np

if __name__ == '__main__':
    
    numpy_array = []
    x, y = input().split()
    for row in range(int(x)):
        inner_list =[]
        for col in range(int(y)):
            # print('inside inner')
            x1 = input()
            inner_list.append(int(x1))
        numpy_array.append(inner_list)

    # print(numpy_array)

    init_array = np.array(numpy_array)
    min_array = np.min(init_array, axis = 1)
    print(max(min_array))
