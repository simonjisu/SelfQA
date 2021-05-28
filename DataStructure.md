- [Array](#array)
- [Tuple](#tuple)
- [List](#list)
- [Set](#set)
- [Dictionary](#dictionary)
- [Linked Lists](#linked-lists)
- [Stacks](#stacks)
- [Queues](#queues)
- [Hash Tables](#hash-tables)

---

# Array

컴퓨터 과학에서 배열(array)은 번호(인덱스)와 번호에 대응하는 데이터들로 이루어진 자료 구조

- 특징: fixed length
- 만약 array의 길이를 변경하려면? array resizing 해야하는데 비용이 생김(memory wastage & memory shortage)
  - Memory wastage: If it contains only n(\<\< N) valid elements
  - Memory shortage: If it wants to contain more than N elements

# Tuple

순서가 있는 데이터를 담는 자료구조

- python

  ```python
  >>> type((1, 2, 3))
  <class 'tuple'>
  ```

- 특징: immutable(한 번 생성하면 데이터를 바꿀 수 없음), ordered, iterable, subscriptable

  ```python
  >>> x = (1, 2, 3)
  >>> x[2] = 4
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  ```

# List
 
순서가 있는 데이터를 담는 자료 구조

- python

  ```python
  >>> type([1, 2, 3])
  <class 'list'>
  ```

- 특징: mutable(생성 후에도 데이터를 바꿀 수 있음), ordered, iterable, subscriptable

# Set

정렬되지 않고(unordered) 고유한(distinct) 데이터으로 이루어진 자료 구조

- python

  ```python
  >>> type({1, 2, 3})
  <class 'set'>
  ```

- 특징: mutable, [unordered](https://stackoverflow.com/questions/12165200/order-of-unordered-python-sets), iterable

# Dictionary

중복되지 않는 key와 value 쌍을 데이터로 가진 정렬되지 않은(unordered) 변경가능한(mutable) 자료구조

- python

  ```python
  >>> type({"a": 1, "b": 2})
  <class 'dict'>
  ```

- 특징: mutable, unordered, iterable

# Linked Lists

[전순서 집합](https://en.wikipedia.org/wiki/Total_order)(linear order) 특징을 가진, 즉 데이터가 순서를 가지는 자료 구조

- 특징: Linked Node object는 다음 Linked Node object와 pointer에 의해 연결되어 있음
- Doubly Linked Lists(노드 앞뒤로 연결됨), Circular Lists(마지막 노드가 첫 노드에 연결되고, 첫 노드가 마지막 노드에 연결됨)
- Sentinals: 더미 오브젝트, 경계 조건을 조금 더 완화하는 역할을 한다.
- Python: 
  - [Single Linked List Code](codes/datastructure/sll.py#L12)
  - [Doubly Linked List Code](codes/datastructure/dll.py#L12)
  - [Circular Linked List Code](codes/datastructure/cll.py#L12)

# Stacks

다이나믹한 Sets, LIFO(last-in, first-out)구조

- Methods: push(데이터를 넣는다), pop(가장 최근에 넣은 데이터를 제거한다)
- Application: Undo Function
- Python: [Stack Code](codes/datastructure/stackandqueue.py#L73)

# Queues

다이나믹한 Sets, FIFO(first-in, first-out)구조

- Methods: enqueue(데이터를 제일 뒷쪽에 넣는다), dequeue(제일 처음에 넣었던 데이터 제거한다)
- Application: Single resource requests(CPU task scheduling)
- Python: [Queue Code](codes/datastructure/stackandqueue.py#L103)

# Hash Tables

키(key)를 값(value)에 매핑할 수 있는 구조인, [연관 배열](https://ko.wikipedia.org/wiki/%EC%97%B0%EA%B4%80_%EB%B0%B0%EC%97%B4)(associative array) 추가에 사용되는 자료 구조

- hash function을 사용하여 key가 차지할 슬롯(slot)를 결정한다. (무한한 고유한 키를 만들 수 없기 때문)
- 충돌(collision): hash function을 통해 두 개의 키(`k1`, `k2`)가 같은 해시 키 값 `h(k1) = h(k2)`를 가질 경우
- 체이닝(chaining): 키를 저장하는 슬롯(slot)를 linked list로 만듬
  - 주의점: 최악의 경우 모든 key가 한 linked list에 저장됨, 이를 피해야함
  - 좋은 hash function 예시: multiplication - `floor(m * (k*A mod 1))` , division: `k mod m`(단 m=2의 멱집합은 피하는게 좋음, 소수가 좋음)
- Python: [Hash Table Code](codes/datastructure/hashtable.py#L56)
