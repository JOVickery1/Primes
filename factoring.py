#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:58:57 2023

@author: jamesvickery
"""

from math import sqrt

while True:
    
    print()
    n = int(input("Enter number: "))
    
    factors = []
    
    primeflag = True
    
    if n == 1:
        primeflag = False
    
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                primeflag=False
                factors.append(i)
                factors.append(int(n/i))
                #break;
        
    if primeflag == True:
        print()
        print(str(n)+" is prime")
        
    else:
        factors.sort()
        print()
        print(factors)