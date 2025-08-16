from collections import defaultdict

def sort_dict(udict : defaultdict):
    keys = list(udict.keys())
    
    n = len(keys)
    k = 0
    
    while k < n:
        for i in range(n - 1 - k):
            if udict[keys[i]] < udict[keys[i + 1]]:
                keys[i + 1], keys[i] = keys[i], keys[i + 1]
            elif udict[keys[i]] == udict[keys[i + 1]]:
                while i + 1 < n and keys[i] > keys[i + 1] and udict[keys[i]] == udict[keys[i + 1]]:
                    keys[i + 1], keys[i] = keys[i], keys[i + 1]

                    i += 1
                    
                
        k += 1
    
    return keys


def DishPrepareOrder(order_list):
    order_count = defaultdict(int)
    for order in order_list:
        order_count[order] += 1

    
    sorted_dict_keys = sort_dict(order_count)
        
    return sorted_dict_keys

nums = eval(input())
print(DishPrepareOrder(nums))