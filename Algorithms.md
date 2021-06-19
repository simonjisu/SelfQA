
- [Sorting](#sorting)
  - [Selection](#selection)
  - [Insertion](#insertion)
  - [Bubble](#bubble)
  - [Merge Sort](#merge-sort)
  - [Quick Sort](#quick-sort)
  - [Sorting 비교](#sorting-비교)
- [Search](#search)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
- [Tree Traversal](#tree-traversal)
  - [Depth-First](#depth-first)
  - [Breadth-First](#breadth-first)

# Sorting

## Selection

- 선택 정렬(Selection Sort)은 원소들중 가장 작은 원소를 찾아 첫번째 자리부터 채워넣는 것이다. 마지막 한자리가 남을 때까지 알고리즘은 계속된다.
- 복잡도: O(N^2)
- python

    ```python
    def selection_sort(l: list) -> list:
        """
        Selection Sort
        Args: 
            l: input list
        Return:
            sorted list by ascending
        """
        def swap(p, q):
            """swap p-th element and q-th element"""
            t = l[p]
            l[p] = l[q]
            l[q] = t
        n = len(l)
        for j in range(n-1):
            smallest_idx = j
            for i in range(j+1, n):
                if l[smallest_idx] > l[i]:
                    smallest_idx = i
            swap(j, smallest_idx)
        return l
    ```

## Insertion

- 삽입 정렬(Insertion Sort)은 정렬된 부분과 정렬되지 않는 부분을 따로 두어 정렬되지 않은 부분의 첫 원소부터 차례대로 정렬된 부분으로 넣는 알고리즘
- 복잡도: O(N^2)
- python

    ```python
    def insertion_sort(l: list) -> list:
        """
        Insertion Sort
        Args: 
            l: input list
        Return:
            sorted list by ascending
        """
        n = len(l)
        for j in range(1, n):
            value = l[j]
            i = j
            while i > 0 and value < l[i-1]:
                l[i] = l[i-1]
                i -= 1
            l[i] = value

        return l
    ```

## Bubble

- 버블 정렬(Bubble Sort)은 각 스텝에서 서로 인접한(adjacent) 두 원소를 크기를 비교하여 바르지 않은 순서일 경우 두 원소를 교환(swap)하는 알고리즘
- 복잡도: O(N^2)
- python

    ```python
    def bubble_sort(l: list) -> list:
        """
        Bubble Sort
        Args: 
            l: input list
        Return:
            sorted list by ascending
        """
        def swap(p, q):
            """swap p-th element and q-th element"""
            t = l[p]
            l[p] = l[q]
            l[q] = t
        n = len(l)
        for i in range(n):  
            for j in range(n-1-i):
                if l[j] > l[j+1]:
                    swap(j, j+1)
        return l
  ```

## Merge Sort

- 합병 정렬(Merge Sort)의 아이디어는 분할정복(devide & conquer)
    - Devide 들어온 입력을 반으로 쪼갠 다음에 반으로 나눠진 입력에 대해서 재귀적으로 합병 정렬을 실행 한다.
    - Conquer 두 개의 정렬된 데이터가 입력으로 들어온다. 그러면 새로운 공간에 두 입력을 하나로 합치(merge)면서 정렬한다.
- 복잡도: O(N log_2 N)
- python
    ```python
    def merge_sort(l):
    """
    Merge Sort
    Args: 
        l: input list
    Return:
        sorted list by ascending
    """
    def merge(left, right):
        """
        Merge two sorted list into one
        Args: 
            left, right: sorted list
        Return:
            sorted list
        """
        li = []
        idx_left, idx_right = 0, 0
        len_left, len_right = len(left), len(right)
        while (idx_left < len_left) and (idx_right < len_right):
            if left[idx_left] < right[idx_right]:
                li.append(left[idx_left])
                idx_left += 1
            else:
                li.append(right[idx_right])
                idx_right += 1
        while idx_left < len_left:
            li.append(left[idx_left])
            idx_left += 1
        while idx_right < len_right:
            li.append(right[idx_right])
            idx_right += 1
        return li
    
    if len(l) in (0, 1):
        return l
    idx_mid = int(len(l)/2)
    left = merge_sort(l[:idx_mid])
    right = merge_sort(l[idx_mid:])
    li = merge(left, right)
    return li
    
    ```

## Quick Sort

- 분할정복(devide & conquer) 알고리즘
    - Devide: 피벗(pivot)원소를 골라서, 입력을 피벗원소보다 작은 쪽은 왼쪽, 피벗보다 큰쪽은 오른쪽으로 나눈다. 따라서 무조건 반으로 나뉘는 합병 정렬과 달리 좌우 입력의 길이가 달라질 수 도 있다.
    - Conquer: 재귀적으로 두 파트를 다시 분할하고 정렬 한다.
- inplace 알고리즘
- 복잡도: O(N log_2 N)
- python
    ```python
    def quick_sort(l):
    """
    Quick Sort
    Args: 
        l: input list
    Return:
        sorted list by ascending
    """
    def partition(l, low, high):
        """
        Partitioin the list into small and large part by pivot
        Args:
            l: input list
            low: lowest index of the partitioned list
            high: highest index of the partitioned list
        Return:
            pivot index in the list
        """
        def swap(p, q):
            """swap p-th element and q-th element"""
            t = l[p]
            l[p] = l[q]
            l[q] = t
        pivot = l[low]
        m = low
        for j in range(low+1, high+1):
            if l[j] < pivot:
                m += 1
                swap(j, m)
        swap(low, m)
        return m
    
    def sort(l, low, high):
        """
        stop sorting when the `low` index is higher then `high` index 
        """
        if low < high:
            pivot_idx = partition(l, low, high)
            sort(l, low, pivot_idx-1)
            sort(l, pivot_idx+1, high)
        return None
    
    sort(l, 0, len(l)-1)
    return l
    ```

## Sorting 비교

|Sort| Worst T(N)| Best T(N)| Stability | Inplace|
|--|--|--|--|--|--|
|Bubble| O(N^2)| O(N^2)| Yes | Yes |
|Insertion| O(N^2)| O(N^2)| Yes | Yes |
|Selection| O(N^2)| O(N^2)| No | Yes |
|Merge| O(N log N)| O(N log N)| Yes | No |
|Quick| O(N^2)| O(N log N)| No | Yes |

- Stability: 정렬 후에도 기존 입력 시퀀스의 특성과 순서를 유지하는지

# Search

## Linear Search

- 순서대로 원소를 찾는것
- python
    ```python
    def linear_search(l, e):
        idx = -1
        for i in range(len(l)):
            if l[i] == e:
                idx = i 
                break
        return idx
    ```
- 복잡도:
    - sorted: O(N)
    - not sorted: O(N)

## Binary Search

- 분할정복(devide & conquer) 알고리즘
- 찾는 원소가 현재 인덱스의 원소보다 작으면 왼쪽, 크면 오른쪽 찾기
- python
    ```python
    def binary_search(l, e):
        left_p = 0
        right_p = len(l)-1
        while left_p < right_p:
            i = int((left_p + right_p) / 2)
            if e == l[i]:
                return i
            elif e < l[i]:
                right_p = i-1
            else: # e > l[i]
                left_p = i+1
        return -1

    def binary_search(l, e):
        """recursive"""
        def _search(l, left_p, right_p, e):
            if left > right:
                return -1
            i = int((left_p + right_p) / 2)
            if e == l[i]:
                return i
            elif e < l[i]:
                right_p = i-1
                i = _search(l, left_p, right_p, e)
            else: # e > l[i]
                left_p = i+1
                i = _search(l, left_p, right_p, e)
            return i
        return _search(l, 0, len(l)-1, e)
    ```

- 복잡도:
    - sorted: O(log_2 N)
    - not sorted: sort after search O(N log_2 N) + O(log_2 N) = O(N log_2 N) 

# Tree Traversal

## Depth-First

## Breadth-First