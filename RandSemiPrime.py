#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:05:05 2023

@author: jamesvickery
"""

from random import randint

from math import sqrt

primes = []

m= int(input("Random semiprime less than what number? "))
 
for n in range(0,int(sqrt(m))):
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
    a = input("Press Enter to generate a 'random' semi-prime number")
        
    c=randint(0,len(primes)-1)
    d=randint(0,len(primes)-1)
    while c == d:
        d=randint(0,len(primes)-1)
    
    print()
    print(primes[c]*primes[d])
    print()
