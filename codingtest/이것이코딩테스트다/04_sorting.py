__doc__ = """
# Chapter 6 정렬
"""

from typing import List, Tuple

def fromTopToBottom(N: int, data: List[int]) -> List[int]:
    return sorted(data, reverse=True)

def scoreSorting(N, data:List[Tuple[str, int]]) -> List[str]:
    return list(map(lambda x: x[0], sorted(data, key=lambda x: x[1])))

def swapArrayElement(N: int, K: int, data: List[List[int]]) -> int:
    """
    K번 바꿔치기 해서 A 배열 합의 최댓값을 출력 

    Args:
        N (int): Number of elements in array
        K (int): 바꿔치기 횟수
        data (List[List[int]]): 배열 A, B

    Returns:
        int: 배열 A의 합
    """    
    A = data[0]
    B = data[1]
    A.sort()
    B.sort(reverse=True)
    count = 0
    for i in range(N):
        if count >= K:
            break
        A[i] = B[i]
        count += 1
    return sum(A)



if __name__ == "__main__":
    print("Example 6.2")
    N = 3
    data = [15, 27, 12]
    print(fromTopToBottom(N, data))

    print("Example 6.3")
    N = 2
    data = [('홍길동', 95), ('이순신', 77)]
    print(scoreSorting(N, data))

    print("Example 6.3")
    N, K = 5, 3
    data = [[1, 2, 5, 4, 3], [5, 5, 6, 6, 5]]
    print(swapArrayElement(N, K, data))