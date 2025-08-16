def findLargest(L):
    n = len(L)
    left = 0
    right = n - 1
    mid = n // 2

    while not(L[mid] > L[mid + 1]):

        if L[mid] < L[0]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2       
    return L[mid]

nums = list()
with open("C:/Users/PC-Kanak/Documents/University/OB/PDSA/week2/GrPA2_output.txt", "r") as file:
    for line in file:
        line = int(line)
        nums.append(line)

print(findLargest(nums))
