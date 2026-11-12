class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # count the sides of each land cell that is either edge or water
        m = len(grid)
        n = len(grid[0])
        p = 0
        for row in range(m):
            for col in range(n):
                # at a water cell so skip
                if grid[row][col] == 0:
                    continue
                # at a land cell so see if its bordering the edge or water
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    # spot around it is within bounds so see if its water
                    if new_row < m and new_row >= 0 and new_col < n and new_col >= 0:
                        if grid[new_row][new_col] == 0:
                            p += 1
                    # cell around it is out of bounds so thats a perimiter
                    else:
                        p += 1
        
        return p
