__doc__ = """
# Chapter 9 최단경로

- 다익스트라 최단경로 알고리즘
- 플로이드 워셜 알고리즘
- 벨만 포드 알고리즘
"""

from typing import List

def dijkstraMethod1(graph, start):
    INF = int(1e9) # float("inf")
    
    return 


if __name__ == "__main__":
    graph = {
        1: [(2, 2), (3, 5), (4, 1)],
        2: [(3, 3), (4, 2)],
        3: [(2, 3), (6, 5)],
        4: [(3, 3), (5, 1)],
        5: [(3, 1), (6, 2)],
    }