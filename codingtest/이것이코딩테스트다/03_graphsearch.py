__doc__ = """
# Chapter 5 DFS/DBS

- DFS: stack + recursion
- BFS: queue + while

"""

from typing import List
from collections import deque

def dfs(graph: List[List[int]], v: int, visited: List[bool]) -> None:
    """
    DFS: stack + recursion

    Args:
        graph (List[List[int]]): graph
        v (int): node
        visited (List[bool]): container
    """    
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph: List[List[int]], start: int, visited: List[bool]) -> None:
    """
    BFS: queue + while

    Args:
        graph (List[List[int]]): graph
        start (int): start number
        visited (List[bool]): container
    """    
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def countIceCream(N: int, M: int, data: List[List[int]]) -> int:
    """

    Args:
        N (int): row number
        M (int): col number
        data (List[List[int]]): map

    Returns:
        int: count
    """    
    def dfs(x, y):
        if x <= -1 or x >= N or y <= -1 or y >= M:
            return False
        if data[x][y] == 0:
            # meet the hole
            data[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
    
    res = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                print(f"Start coordinate: {i, j}")
                print(f"Map:")
                for line in data:
                    print("".join(map(str, line)))
                res += 1
    return res

def escapeMaze(N: int, M: int, data: List[List[int]]) -> int:
    """

    Args:
        N (int): row number
        M (int): col number
        data (List[List[int]]): map

    Returns:
        int: count
    """    
    steps = [(-1, 0), (0, +1), (0, -1), (+1, 0)]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in steps:
            x_next = x + dx
            y_next = y + dy
            if x_next <= -1 or x_next >= N or y_next <= -1 or y_next >= M:
                continue
            if data[x_next][y_next] == 1:
                data[x_next][y_next] += data[x][y]
                queue.append((x_next, y_next))
                print(f"Coordinate: {x, y}")
                print("Map:")
                for line in data:
                    print("".join([f" {num}" if len(num) == 1 else num for num in list(map(str, line))]))
    
    return data[N-1][M-1]
    
if __name__ == "__main__":

    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    print("DFS")
    visited = [False]*9
    print(dfs(graph, 1, visited))
    print("BFS")
    visited = [False]*9
    print(bfs(graph, 1, visited))

    print("Example 5.3")
    N, M = 5, 14
    data = """
    00000111100000
    11111101111110
    11011101101110
    11011101100000
    11011111111111
    """
    print(data)
    data = [list(map(int, list(line.strip()))) for line in data.split() if line.strip() != ""]
    print(countIceCream(N, M, data))

    print("Example 5.4")
    N, M = 5, 6
    data = """
    101010
    111111
    000001
    111111
    111111
    """
    print(data)
    data = [list(map(int, list(line.strip()))) for line in data.split() if line.strip() != ""]
    print(escapeMaze(N, M, data))