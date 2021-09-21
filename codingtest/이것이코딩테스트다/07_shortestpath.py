__doc__ = """
# Chapter 9 최단경로

- 다익스트라 최단경로 알고리즘
    - 그리디, O(N^2)
- 플로이드 워셜 알고리즘
    - 다이나믹 프로그래밍, O(N^3)
- 벨만 포드 알고리즘

힙(Heap) = 우선순위 큐(Priority Queue)
"""

from typing import List, Dict, Tuple
import heapq

def dijkstraMethod1(N: int, M: int, graph: Dict[int, List[Tuple[int, int]]], start: int):
    """
    Dijkstra Algorithm Method 1: O(V^2)

    Args:
        N (int): Node numbers
        M (int): Edge numbers
        graph (Dict[int, List[Tuple[int, int]]]): Graph
        start (int): start node (index from 1)
    """
    
    INF = int(1e9) # float("inf")
    visited = [False] * N
    distance = [INF] * N


    def getSmallestNode(distance, visited, N):
        min_value = INF
        index = 0
        for i in range(N):
            if not visited[i] and distance[i] < min_value:
                min_value = distance[i]
                index = i
        return index      

    # start
    visited[start] = True
    distance[start] = 0
    for node, dis in graph[start]:
        distance[node] = dis
    print(f"First Visit {start}")
    print(f"  Distance: {distance}")
    for i in range(N-1):
        now = getSmallestNode(distance, visited, N)
        print(f"({i}) Smallest distance node: {now}")
        visited[now] = True
        for node, dis in graph[now]:
            cost = distance[now] + dis
            if cost < distance[node]:
                distance[node] = cost

        print(f"  Visited: {visited}")
        print(f"  Distance: {distance}")

    for i in range(N):
        if distance[i] == INF:
            print(f"(Node {i}) Infty", end=" ")
        else:
            print(f"(Node {i}) {distance[i]}", end=" ")
            
    return 


def dijkstraMethod2(N: int, M: int, graph: Dict[int, List[Tuple[int, int]]], start: int):
    """
    Dijkstra Algorithm Method 2: O(E\logV)

    Args:
        N (int): Node numbers
        M (int): Edge numbers
        graph (Dict[int, List[Tuple[int, int]]]): Graph
        start (int): start node (index from 0)
    """
    INF = int(1e9) # float("inf")
    distance = [INF] * N
    distance[start] = 0    
    q = []
    
    heapq.heappush(q, (0, start))
    while q:
        print(f"Current Queue Status: {q}")
        cur_dist, now = heapq.heappop(q)
        print(f"Current Node: {now}")
        # ignore if larger than min distance
        if distance[now] < cur_dist: 
            continue

        for node, dis in graph[now]:
            cost = cur_dist + dis
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

        print(f"  Distance: {distance}")

    for i in range(N):
        if distance[i] == INF:
            print(f"(Node {i}) Infty", end=" ")
        else:
            print(f"(Node {i}) {distance[i]}", end=" ")

    return


def printGraph(g):
    for x in g:
        print(x)

def floydWarshall(N: int, M: int, graph: Dict[int, List[Tuple[int, int]]]):
    """
    D_{ab} = \min(D_{ab}, D_{ak} + D_{kb})

    Args:
        N (int): Node numbers
        M (int): Edge numbers
        graph (Dict[int, List[Tuple[int, int]]]): Graph
    """    
    INF = int(1e9) # float("inf")
    distance = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                distance[i][j] = 0
    for i, links in graph.items():
        for j, dis in links:
            distance[i][j] = dis
    printGraph(distance)

    for k in range(N):
        for a in range(N):
            for b in range(N):
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
    
    for a in range(N):
        for b in range(N):
            if distance[a][b] == INF:
                print(f"(Node {a} -> {b}) Infty", end=" ")
            else:
                print(f"(Node {a} -> {b}) {distance[a][b]}", end=" ")
        print()

    return

if __name__ == "__main__":
    N, M = 6, 11
    graph = {
        0: [(1, 2), (2, 5), (3, 1)],
        1: [(2, 3), (3, 2)],
        2: [(1, 3), (5, 5)],
        3: [(2, 3), (4, 1)],
        4: [(2, 1), (5, 2)],
        5: []
    }
    print()
    print("=== dijkstra Method 1 ===")
    dijkstraMethod1(N, M, graph, start=0)
    print()
    print("=== dijkstra Method 2 ===")
    dijkstraMethod2(N, M, graph, start=0)
    print()
    print("=== floyd warshall Method ===")


    N, M = 4, 7
    graph = {
        0: [(1, 4), (3, 6)],
        1: [(0, 3), (2, 7)],
        2: [(0, 5), (3, 4)],
        3: [(2, 2)],
    }

    floydWarshall(N, M, graph)