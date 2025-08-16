import numpy as np

def MaxCoinPath(M, x1, y1, x2, y2):
    
    coins = np.zeros((x2 - x1, y2 - y1))
    M = np.asarray(M)
    coins = findMaxCoinPath(M[x1:x2+1, y1:y2+1], coins)

    return int(coins[-1][-1])

def findMaxCoinPath(M, coins):
    x, y = M.shape
    MaxCoins = np.zeros((x, y))
    MaxCoins[0][0] = M[0][0]

    # Diagonally solve all terms
    for n in range(1, x + y - 2):
        for i in range(n + 1):
            j = n - i
            if j >= y or i >= x:
                continue

            if i == 0:
                MaxCoins[0][j] = M[0][j] + MaxCoins[0][j - 1]
                continue
            if j == 0:
                MaxCoins[i][0] = M[i][0] + MaxCoins[i - 1][0]
                continue

            MaxCoins[i][j] = M[i][j] + max(MaxCoins[i-1][j], MaxCoins[i][j-1])
    
    MaxCoins[x-1][y-1] = M[x-1][y-1] + max(MaxCoins[x-2][y-1], MaxCoins[x-1][y-2])
    return MaxCoins




# M = eval(input())
# (x1,y1)=eval(input())
# (x2,y2) = eval(input())

M = [[2,1,3,2,5],
     [3,5,2,4,6],
     [7,6,1,3,2],
     [2,9,4,7,8],
     [1,4,5,11,3]]
x1, y1 = (0,0)
x2, y2 = (4,4)
print(MaxCoinPath(M,x1,y1,x2,y2))