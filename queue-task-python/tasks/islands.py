from typing import List


def get_islands_count(grid: List[List[str]]) -> int:
    """Returns the number of islands in a given grid.

    Hint: you need to go over the grid and 'explore' islands
    one by one, some sort of BFS (using queue) will do.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def bfs(r, c):
        queue = [(r, c)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and grid[nx][ny] == "1"
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                visited[r][c] = True
                bfs(r, c)
                count += 1

    return count
