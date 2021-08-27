
from typing import List

def giveChanges(n: int):
    """
    # Example 3.1

    Args:
        n (int): 거스름돈 총액
    Return:
        count: 거슬러 줘야할 최소 동전의 갯수
    """
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin
        print(f"Coin Type: {coin}, Count: {count}, Left: {n}")
    return count

def lawOfLargeNumbers(N: int, M: int, K: int, li: List[int]):
    li.sort()
    check = [(li[-1], 0), (li[-2], 0)]
    res = 0
    idx = 0
    





if __name__ == "__main__":

    print("Example 3.1")
    print(f"Minima Coins: {giveChanges(1260)}")
    print()