#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:55:33 2023

@author: jamesvickery
"""


from random import randint

from math import sqrt

m= int(input("Random prime less than what number? "))

primes = []
 
for n in range(0,m):
    primeflag = True
    
    if n == 1 or n==0:
        primeflag = False
        
    elif n%2==0:
        primeflag = False
    
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                primeflag=False
                break;
        
    if primeflag == True:
       primes.append(n)

print()

while True:
    a = input("Random Prime Number? ")
        
    c=randint(0,len(primes)-1)
    
    print()
    print(primes[c])
    print()