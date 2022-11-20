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
