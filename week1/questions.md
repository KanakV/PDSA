# Coding Questions

---

## Q1 – Minimum Difference in Subset

Write a function `find_Min_Difference(L, P)` that accepts a list `L` of integers and `P` (positive integer) where the size of `L` is greater than `P`. The task is to pick `P` different elements from the list `L`, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of `P` elements. The function returns this minimum difference value.  

**Note** - The list can contain more than one subset of `P` elements that have the same minimum difference value.

---

## Q2 – Goldbach’s Conjecture

Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. It states that every even number greater than 2 is the sum of two prime numbers.

Write a function `Goldbach(n)` where `n` is a positive even number (`n > 2`) that returns a list of tuples. In each tuple `(a, b)` where `a <= b`, `a` and `b` should be prime numbers and the sum of `a` and `b` should be equal to `n`.

---

## Q3 – Odd One Out

Write a function named `odd_one(L)` that accepts a list `L` as argument. Except for one element, all other elements in `L` are of the same data type. The function `odd_one` should return the data type of this odd element.  

For example, if `L` is equal to `[1, 2, 3.4, 5, 10]`, then the function should return the string `float`. This is because the element `3.4` is the odd one here, all other elements are integers.

**Note**  
1. `L` has at least three elements.  
2. For each test case, the elements in the list will only be of one of these four types: `int`, `float`, `str`, `bool`.  
3. The function must return one of these four strings: `int`, `float`, `str`, `bool`.  
4. Hint: `type(1) == int` evaluates to True.  

---
