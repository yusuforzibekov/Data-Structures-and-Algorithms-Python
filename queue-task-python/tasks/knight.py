from typing import List
from collections import deque


def get_minimum_knight_moves(chessboard: List[List[str]]) -> int:
    """Returns the minimum number of knight moves to reach the destination point."""
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    rows, cols = 8, 8
    start = end = None

    for r in range(rows):
        for c in range(cols):
            if chessboard[r][c] == "K":
                start = (r, c)
            elif chessboard[r][c] == "D":
                end = (r, c)

    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    while queue:
        x, y, d = queue.popleft()
        if (x, y) == end:
            return d
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and chessboard[nx][ny] != "O"
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny, d + 1))

    return -1  # Should never reach here as per problem statement
