import math

def Goldbach(n : int):
    nums = list()
    for i in range(3, int(n / 2) + 1):
        if is_prime(i) and is_prime(n - i):
            nums.append((i, n - i))
    return nums

def is_prime(n):
	(result, i) = (True, 2)
	while (result and (i <= math.sqrt(n))):
		if (n%i) == 0:
			result = False
		i = i+1
	return(result)

n=int(input())
print(sorted(Goldbach(n)))