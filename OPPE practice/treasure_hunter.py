def max_treasure(house):
    n = len(house)
    maxGold = []
    for i in range(n):
        maxGold[i] = None

    Tmax = 0
    for i, treasure in enumerate(house):
        if maxGold[i] is not None:
            Tmax = max()

        Tmax += max(house[i] + maxGold[i+2], maxGold[i+1])
    

    
    ...


house = [1, 3, 3, 4]

print(max_treasure(house))


