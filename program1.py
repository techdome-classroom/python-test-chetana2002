class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        count = 0
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the current cell contains a landmass, perform a depth-first search to mark all connected landmasses
                if grid[i][j] == 'L':
                    # Increment the counter for the number of islands
                    self.dfs(grid, i, j)
                    count += 1
        
        
        # Return the number of distinct islands
        return count

    def dfs(self, grid, i, j):
        # Define the boundaries of the grid
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='L':
            return
        
        # Mark the current cell as visited by changing it to '#'
        grid[i][j] = '#'
        # Recursively visit neighboring cells that are also landmasses
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    #    write your code here
                    
        return 0