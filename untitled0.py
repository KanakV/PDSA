# -*- coding: utf-8 -*-
"""
Created on Fri May 16 15:28:17 2025

@author: PC-Kanak
"""

import math

def Twin_Primes(n, m):
    twin_primes = list()
    
    if (n % 2 == 1):
        n = n - 1
    
    for i in range(n + 2, m , 2):
        if check_prime(i - 1) and check_prime(i + 1):
            twin_primes.append((i - 1, i + 1))
    return twin_primes

def check_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
m = int(input())
print(sorted(Twin_Primes(n, m)))