
def max_tiling(n, grid):

    max_score = [vertical(grid, 0)] * n
    if n == 1:
        return max_score[0]
    
    max_score[1] = max(max_score[0] + vertical(grid, 1), horizontal(grid, 1))
    
    for i in range(2, n):
        max_score[i] = max(max_score[i-1]+vertical(grid,i), 
            max_score[i-2] + horizontal(grid, i))
    
    return max(max_score)

def horizontal(grid, end):
    return abs(grid[0][end-1] - grid[0][end]) + abs(grid[1][end-1] - grid[1][end])
    

def vertical(grid, i):
    return abs(grid[0][i] - grid[1][i])

# n = int(input())
# grid = []

# for i in range(2):
#     inp = input().split()
#     for i in range(n):
#         inp[i] = int(inp[i])
#     grid.append(inp)


n = 2
grid = [
    [8, 6, 2, 3],
    [9, 7, 1, 2]
]
grid = [[1],
        [2]
]
grid = [[1, 3],
        [4, 5]
]

print(max_tiling(n, grid))