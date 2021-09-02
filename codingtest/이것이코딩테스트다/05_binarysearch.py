__doc__ = """
# Chapter 8 이진 탐색

전제조건: 데이터가 정렬되어 있어야함
"""

from typing import List, Tuple

def binarySearchRecursion(array: List[int], target: int, start: int, end: int) -> int:
    if start > end:
        # end recursion when start index > end index
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchRecursion(array, target, start, mid-1)
    else:
        return binarySearchRecursion(array, target, mid+1, end)

def binarySearchWhile(array: List[int], target: int, start: int, end: int) -> int:
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def findParts(N: int, M: int, data: List[int]) -> List[str]:
    """
    Example 7.2

    Args:
        N (int): 가게 부품 갯수
        M (int): 요청 부품 갯수
        data (List[int]): 0: 가게 부품 리스트, 1: 요청 부품 리스트

    Returns:
        List[str]: 있으면 yes, 없으면 no
    """
    A = data[0]
    B = data[1]
    # check = []
    # for x in B:
    #     if x in A:
    #         check.append(True)
    # return sum(check) == M

    A.sort()
    return ['yes' if binarySearchRecursion(A, x, 0, N-1) != None else 'no' for x in B]

def makeTteokbokki(N: int, M: int, data: List[int]) -> int:
    """
    Example 7.3

    Args:
        N (int): 떡의 개수
        M (int): 요청한 떡의 길이
        data (List[int]): 떡

    Returns:
        int: 절단기 설정 높이의 최댓값
    """
    # binary seach on height of machine
    def getRemain(data, H):
        return sum(map(lambda x: 0 if (x - H) < 0 else (x - H), data))
    res = 0
    end = max(data)
    start = 0
    while start <= end:
        H = (start + end) // 2
        print(f"min, max height = {start, end}, H={H}, remain={getRemain(data, H)}")
        if getRemain(data, H) < M:
            end = H - 1
        else:
            res = H
            start = H + 1
        
    return res




if __name__ == "__main__":
    
    array = list(range(1, 20, 2))
    target = 7
    print("Binary Search: Recursion")
    print(binarySearchRecursion(array, target, 0, len(array)-1))
    print("Binary Search: While")
    print(binarySearchWhile(array, target, 0, len(array)-1))

    print("Example 7.2")
    N, M, = 5, 3
    data = [[8, 3, 7, 9, 2], [5, 7, 9]]
    print(findParts(N, M, data))

    print("Example 7.3")
    N, M, = 4, 6
    data = [19, 15, 10, 17]
    print(makeTteokbokki(N, M, data))