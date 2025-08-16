def minmax(a, b):
    n = len(a)
    
    for i in range(n):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
    
    num1 = max(a)
    num2 = max(b)
    
    return num1 * num2



a = eval(input())
b = eval(input())
print(minmax(a,b))