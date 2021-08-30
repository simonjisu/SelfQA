__doc__ = """
# Chapter 4 구현

# 유형

1. 완전탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
2. 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계식 차례대로 수행

"""

from typing import List, Tuple, Union

def upDownLeftRight(N: int, data: List[str]) -> Union[Tuple[int], List[int]]:
    """
    # Example 4.1.1

    가장 왼쪽 위 좌표, 시작좌표 = (1, 1), 가장 오른쪽 아래 좌표 = (N, N)
    갈 수 없는 이동 문자는 무시하기
    
    Args:
        N (int): 지도 크기
        data (List[str]): 이동 문자열

    Returns:
        Union[Tuple[int], List[int]]: 최종 좌표
    """
    r, c = 1, 1
    for l in data:
        if l == "R" and c < N:
            c += 1
        elif l == "L" and c > 1:
            c -= 1
        elif l == "U" and r > 1:
            r -= 1
        elif l == "D" and r < N:
            r += 1
    return r, c

def timeContainsThree(N: int) -> int:
    """
    # Example 4.1.2

    Args:
        N (int): 시각

    Returns:
        int: 3 이 포함된 횟수
    """
    total_secs = (N+1) * 60 * 60

    counts = 0
    while total_secs > 0:
        h = total_secs // (60 * 60)
        m = (total_secs - h * 60 * 60) // 60
        s = total_secs - h * 60 * 60 - m * 60
        time_str = f"{h-1:02d}{59 if m-1 < 0 else m-1:02d}{59 if s-1 < 0 else s-1:02d}"
        
        if "3" in time_str:
            counts += 1
        total_secs -= 1

    return counts

def knightInRoyal(coor:str) -> int:
    """
    # Example 4.2

    Args:
        coor (str): 체스판 좌표

    Returns:
        int: 나이트가 이동할 수 있는 경우의 수
    """
    steps = [(-2, -1), (-1, -2), (-2, +1), (-1, +2), (+1, +2), (+2, +1), (+1, -2), (+2, -1)]
    coor_dict = {v: k for k, v in dict(enumerate("abcdefgh", 1)).items()}
    r = int(coor[1])
    c = coor_dict[coor[0]]
    count = 0
    for r_step, c_step in steps:
        if r + r_step <= 8 and r + r_step >= 1 and c + c_step >= 1 and c + c_step <= 8:
            count += 1

    return count

def gameDevelopment(N: int, M:int, status: Tuple[int], gamemap: List[List[int]]) -> int:
    """[summary]
    # Example 4.3
    
    Args:
        N (int): 맵의 행 크기
        M (int): 맵의 칼럼 크기
        status (Tuple[int]): 상태 (X좌표, Y좌표, 방향), 방향은 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)
        gamemap (List[List[int]]): 게임맵, 0(육지), 1(바다)

    Returns:
        int: 이동을 마친 후 방문한 칸의 수
    """
    direc_strs = {0: "북", 1: "동", 2: "남", 3: "서"}
    direc_steps = {0: (-1, 0), 1: (0, +1), 2: (+1, 0), 3: (0, -1)}
    direc_opps = {0: 2, 1: 3, 2: 0, 3: 1}
    visit = [[0 for _ in range(M)] for _ in range(N)]
    r, c, direc = status
    visit[r][c] = 1

    def turnLeft(cur_direc):
        cur_direc -= 1
        if cur_direc == -1:
            return 3
        else:
            return cur_direc
    count = 0
    turn_count = 0
    print(f"Start Direction: {direc_strs[direc]}: {r, c} Count={turn_count}")
    while True:
        direc = turnLeft(direc)
        r_next, c_next = direc_steps[direc]
        print(f"Looking Direction: {direc_strs[direc]}: {r+r_next, c+c_next} Count={turn_count}")
        if gamemap[r+r_next][c+c_next] == 0 and visit[r+r_next][c+c_next] == 0:
            # visit land
            r += r_next
            c += c_next
            count += 1
            visit[r][c] = 1
            turn_count = 0
            print(f" - Visit {r, c}")
            continue
        else:
            turn_count += 1

        if turn_count == 4:
            print(f" - Cur Direction: {direc}")
            direc_opp = direc_opps[direc]
            r_next, c_next = direc_steps[direc]
            if gamemap[r+r_next][c+c_next] == 0:
                # go back 
                r += r_next
                c += c_next
                print(f" - Go Back: {r, c}")
            else:
                # block by sea
                print(f" - Blocked")
                break
            turn_count = 0

    return count

if __name__ == "__main__":

    print("Example 4.1.1")
    N, data = 5, list("RRRUDD")
    print(f"Final Coordinamtes: {upDownLeftRight(N, data)}")
    print()

    print("Example 4.1.2")
    N = 5
    print(f"Number that contains 3 in from {N:02d}:59:59 to 00:00:00 : {timeContainsThree(N)}")
    print()
    
    print("Example 4.2")
    coor = "c2"
    print(f"Counts of possible movements: {knightInRoyal(coor)}")
    print()

    print("Example 4.2")
    N, M = 5, 5
    status = (1, 1, 0)
    gamemap = [
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 1], 
        [1, 1, 0, 1, 1], 
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(f"Counts of possible movements: {gameDevelopment(N, M, status, gamemap)}")
    print()