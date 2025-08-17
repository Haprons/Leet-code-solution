class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r , c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    continue
                else:
                    if (i-1 < 0) or (grid[i-1][j] == 0): perimeter += 1
                    if (j-1 < 0) or (grid[i][j-1] == 0): perimeter += 1
                    if (i+1 == r) or (grid[i+1][j] == 0): perimeter += 1
                    if (j+1 == c) or (grid[i][j+1] == 0): perimeter += 1
        return perimeter