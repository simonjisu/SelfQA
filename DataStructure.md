- [Array](#array)
- [Tuple](#tuple)
- [List](#list)
- [Set](#set)
- [Dictionary](#dictionary)
- Linked Lists
- Stacks
- Queues
- Hash Tables
- Graphs
  - Adjacency Lists
  - Adjacency Matrix
- Trees
  - Binary Trees

---

# Array

컴퓨터 과학에서 배열(array)은 번호(인덱스)와 번호에 대응하는 데이터들로 이루어진 자료 구조

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