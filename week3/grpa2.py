from collections import deque

signs = ["+", "-", "*", "/", "**"]

def EvaluateExpression(exp):
    terms = exp.split()
    
    postfix = deque()
    nums = deque()
    
    for term in terms:
        postfix.append(term)
    
    while len(postfix) >= 1:
        term = postfix.popleft()
        if term in signs:
            b = nums.pop()
            a = nums.pop()
            nums.append(calculate(a, b, term))
        else:
            nums.append(int(term))
    
    return nums.pop()
            
def calculate(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        return a / b
    elif sign == "**":
        return a ** b
    else:
        raise ValueError(f"Unsupported operator: {sign}")

print(float(EvaluateExpression(input())))   