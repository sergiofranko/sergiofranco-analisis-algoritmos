class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    self.sink_island(grid, row, column, rows, columns)

        return islands

    def sink_island(self, grid, start_row, start_column, rows, columns):
        stack = [(start_row, start_column)]
        grid[start_row][start_column] = "0"

        while stack:
            row, column = stack.pop()

            neighbors = [
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1)
            ]

            for next_row, next_column in neighbors:
                inside_grid = (
                    0 <= next_row < rows and
                    0 <= next_column < columns
                )

                if inside_grid and grid[next_row][next_column] == "1":
                    grid[next_row][next_column] = "0"
                    stack.append((next_row, next_column))