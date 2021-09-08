__doc__ = """
# Chapter 9 최단경로

- 다익스트라 최단경로 알고리즘
- 플로이드 워셜 알고리즘
- 벨만 포드 알고리즘
"""

from typing import List, Dict, Tuple

def dijkstraMethod1(N: int, M: int, graph: Dict[int, List[Tuple[int, int]]], start: int):
    """
    Dijkstra Algorithm Method 1

    Args:
        N (int): Node numbers
        M (int): Edge numbers
        graph (Dict[int, List[Tuple[int, int]]]): Graph
        start (int): start node (index from 1)
    """
    
    INF = int(1e9) # float("inf")
    visited = [False] * N
    distance = [INF] * N


    def getSmallestNode():
        min_value = INF
        index = 0
        for i in range(N):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index + 1        

    # start
    visited[start-1] = True
    distance[start-1] = 0
    for node, dis in graph[start]:
        distance[node-1] = dis
        
    

    return 


if __name__ == "__main__":
    graph = {
        1: [(2, 2), (3, 5), (4, 1)],
        2: [(3, 3), (4, 2)],
        3: [(2, 3), (6, 5)],
        4: [(3, 3), (5, 1)],
        5: [(3, 1), (6, 2)],
    }