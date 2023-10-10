import numpy as np

"""
Conway's Game of Life is a popular cellular automaton that 
simulates the evolution of a two-dimensional grid of cells. 
The basic rules of the game of life are:
- Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
"""

def step(grid):
    new_grid   = np.zeros_like(grid)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j)
            count = sum(neighbors)
            if grid[i, j] == 1 and count in [2, 3]:
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and count == 3:
                new_grid[i, j] = 0
    return new_grid


def get_neighbors(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    valid_indices[4] = False  # exclude current cell
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]
    
# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)
new_grid = step(grid)
print(new_grid)  # should be unchanged, but may change due to the bug