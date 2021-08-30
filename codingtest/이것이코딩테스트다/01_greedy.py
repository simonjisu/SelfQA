
__doc__ = """
# Chapter 3 그리디
"""

from typing import List

def giveChanges(n: int) -> int:
    """
    # Example 3.1

    Args:
        n (int): 거스름돈 총액
    Returns:
        int: 거슬러 줘야할 최소 동전의 갯수
    """
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin
        print(f"Coin Type: {coin}, Count: {count}, Left: {n}")
    return count

def lawOfLargeNumbers(N: int, M: int, K: int, data: List[int]) -> int:    
    """
    # Example 3.2

    Args:
        N (int): 리스트 길이 = len(data)
        M (int): 숫자 갯수
        K (int): 최대 반복가능 횟수
        data (List[int]): 데이터

    Returns:
        int: 큰 수의 법칙에 맞는 수
    """    
    data.sort()
    first = data[N-1]
    second = data[N-2]

    # Maximum number of first biggest number
    # f=first, s=second
    # K = 2, [f, f, s]
    # K = 3, [f, f, f, s]
    # K = 4, [f, f, f, f, s]
    count = (M // (K+1)) * K
    # if floor division result is 0, means no M < K+1
    count += M % (K+1)

    result = 0
    result += first * count
    result += second * (M-count)
    return result
    
def cardGameBiggestNumber(N:int, M:int, data: List[List[int]]) -> int:
    """
    # Example 3.3

    Args:
        N (int): 행의 갯수
        M (int): 칼럼의 갯수
        data (List[List[int]]): 행렬 데이터

    Returns:
        int: 뽑을 수 있는 최대 크기의 숫자
    """
    return max([min(row) for row in data])

def untilOne(N:int, K:int) -> int:
    """
    # Example 3.4
    1. N에서 1을 뺀다.
    2. N이 K로 나누어 떨어질 때만, N을 K로 나눈다.

    Args:
        N (int): 어떠한 수
        K (int): 나누어야할 수

    Returns:
        int: 최소 횟수
    """
    count = 0
    while N > 1:        
        if N % K == 0:
            N = int(N / K)
            count += 1
            continue
        N -= 1
        count += 1
    return count


if __name__ == "__main__":

    print("Example 3.1")
    print(f"Minima Coins: {giveChanges(1260)}")
    print()

    print("Example 3.2")
    N, M, K, data = 5, 8, 3, [2, 4, 5 ,4, 6]
    print(f"Number for N={N}, M={M}, K={K}, data={data} is: {lawOfLargeNumbers(N, M, K, data)}")
    print()

    print("Example 3.3")
    N, M, data = 3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
    print(f"Biggest Number for N={N}, M={M}, data={data} is: {cardGameBiggestNumber(N, M, data)}")
    print()
        
    print("Example 3.4")
    N, K = 25, 3
    print(f"Biggest Number for N={N}, K={K} is: {untilOne(N, K)}")
    print()
        