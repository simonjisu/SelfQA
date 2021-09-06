__doc__ = """
# Chapter 9 다이나믹 프로그래밍

조건:
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

점화식
"""
from typing import List, Tuple

def fibonacci(n: int, typ: int=0) -> int:
    """
    Fibonacci Numbers
    $$
    \begin{cases}
    a_{n} &= 1 & n = 1, 2
    a_{n} &= a_{n-1} + a_{n-2} & n >= 3
    \end{cases}
    $$
    
    Args:
        n (int): index

    Returns:
        int: Fibonacci Number
    """
    
    if typ == 0:
        # Recursion
        # unefficient case: O(2^N)
        def fibo(n: int) -> int:
            print(f"f({n})", end=" ")
            if n == 1 or n == 2:
                return 1
            else:
                return fibo(n-1) + fibo(n-2)
        return fibo(n)
    elif typ == 1:    
        # Top-Down
        # d: Memoization
        d = [0]*100
        def fibo(n: int) -> int:
            print(f"f({n})", end=" ")
            if n == 1 or n == 2:
                return 1

            if d[n] != 0:
                return d[n]
            
            d[n] = fibo(n-1) + fibo(n-2)
            return d[n]
        return fibo(n)
    elif typ == 2:
        # Bottom-Up
        # d: DP-Table
        d = [0]*100
        d[1] = 1
        d[2] = 1
        for i in range(3, n+1):
            print(f"f({i})", end=" ")
            d[i] = d[i-1] + d[i-2]
        return d[n]

def intoOne(x: int) -> int:
    """
    a. if x % 5 == 0, x /= 5
    b. if x % 3 == 0, x /= 3
    c. if x % 2 == 0, x /= 2
    d. else, x -= 1

    Args:
        x (int): a number

    Returns:
        int: minimum calculation count
    """
    # a_{i} = min(a_{i-1}, a_{i/2}, a_{i/3}, a_{i/5}) + 1
    # Bottom-up
    d = [0]*30001

    for i in range(2, x+1):
        d[i] = d[i-1]+1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    print(d[:30])
    return d[x]

def antWarrior(N: int, data: List[int]) -> int:
    """
    Example 9.3

    Args:
        N (int): 식량창고의 개수
        data (List[int]): 식량창고에 저장된 식량의 개수

    Returns:
        int: 얻을 수 있는 식량의 최댓값
    """
    # a_{i} = max(a_{i-1}, a_{i-2} + k_i)
    # Bottom-up
    d = [0]*100
    d[0] = data[0]
    d[1] = max(data[0], data[1])
    for i in range(2, N):
        d[i] = max(d[i-1], d[i-2] + data[i])
    print(d[:5])
    return d[N-1]

def floorConstruction(N: int) -> int:
    """
    Example 9.4 

    already filled
    * i-1: 2x1: 1
    * i-2: 1x2: 2, 2x2: 1 / 2x1 는 고려 안함

    Args:
        N (int): 가로 길이

    Returns:
        int: 바닥을 채우는 방법의 수를 769769로 나눈 나머지
    """
    # a_{i} = a_{i-1} + a_{i-2} * 2
    d = [0]*1001
    d[1] = 1
    d[2] = 3
    for i in range(3, N+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796796
    
    print(d[:20])
    return d[N]

def currencyConstruction(N: int, M: int, data: List[int]) -> int:
    """
    Example 9.5
    a_{i}: 화폐 개수, k: 화폐 단위
    a_{i-k} 존재 시, a_{i} = min(a_{i}, a_{i-k}+1)
    a_{i-k} 불가능 시, a_i = -1


    Args:
        N (int): 화폐 종류 개수
        M (int): 목표 화폐 금액
        data (List[int]): 화폐 종류

    Returns:
        int: M원을 만들기 위한 최소한의 화폐 개수
    """
    # Memoization: index as amount
    d = [0] + [10001]*(M)
    for i in range(N):
        for j in range(data[i], M+1):
            if d[j - data[i]] != 10001:
                d[j] = min(d[j], d[j - data[i]] + 1)

    print(d)
    return -1 if d[M] == 10001 else d[M]




if __name__ == "__main__":
    print("Fibonacci Numbers")
    print("Method-1: Recursion")
    print(fibonacci(n=10, typ=0))
    print("Method-2: Top-Down")
    print(fibonacci(n=10, typ=1))
    print("Method-3: Bottom-Up")
    print(fibonacci(n=10, typ=2))

    print("Example 9.2")
    print(intoOne(x=26))

    print("Example 9.3")
    data = [1, 3, 1, 5]
    N = len(data)
    print(antWarrior(N, data))

    print("Example 9.3")
    N = 3
    print(floorConstruction(N))

    print("Example 9.4")
    N, M = 2, 15
    data = [2, 3]
    print(currencyConstruction(N, M, data))
