# Insertion Sort Iterative
def combinationSort(strList):
    L2 = list()

    for i, element in enumerate(strList):
        j = i

        if j == 0:        
            L2.insert(j, element)
            pass

        while (j > 0 and strList[j][0] < strList[j - 1][0]):
            strList[j], strList[j - 1] = strList[j - 1], strList[j]
            j -= 1
        
        L2.insert(j, element)
        while ((int(L2[j][1:]) < int(L2[j - 1][1:])) and L2[j][0] == L2[j - 1][0]):
            L2[j], L2[j - 1] = L2[j - 1], L2[j]
            j -= 1
        
    return (strList, L2)


strList = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]

strList, L2 = combinationSort(strList)
print("L1: ", strList)
print("L2: ", L2)
