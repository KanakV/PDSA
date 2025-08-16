def odd_one(L : list):
    for i, element in enumerate(L):
        L[i] = type(element)
    
    counts = {
        "str"   : L.count(str),
        "int"   : L.count(int),
        "float" : L.count(float),
        "bool"  : L.count(bool)
    }
    
    for key, value in counts.items():
      if value == 1:
        return key

print(odd_one(eval(input().strip())))