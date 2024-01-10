#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:00:56 2023

@author: jamesvickery
"""

from math import sqrt

while True:

    n = int(input("Enter number: "))
    
    b= int(sqrt(n))+1
    
    primeflag = True
    
    if n == 1:
        primeflag = False
        
    elif n%2==0:
        primeflag = False
    
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                primeflag=False
                break;
        
    if primeflag == True:
        print()
        print(str(n)+" is prime")
        print()
        
    else:
        print()
        print(str(n)+" is not prime")
        print()
        