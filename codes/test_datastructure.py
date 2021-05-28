from datastructure import SingleLinkedList, DoublyLinkedList, CircularLinkedList, Stack, Queue, HashTable
from datastructure.stackandqueue import OFError, UFError

def test_list_class(cls):
    print(cls)
    l = cls()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    print(f"Inserting 1, 2, 3 -> {l}")
    print(f"Search 2 -> {l.search(2)}")
    print(f"Search 4 -> {l.search(4)}")
    l.delete(2)
    print(f"Delete 2 -> {l}")
    l.delete(1)
    print(f"Delete 1 -> {l}")
    l.delete(3)
    print(f"Delete 3 -> {l}")

def test_list():
    for cls in [SingleLinkedList, DoublyLinkedList, CircularLinkedList]:
        test_list_class(cls)

def test_stack():
    s = Stack(3)
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Push 1, 2, 3 -> {s}")
    try:
        s.push(4)
    except OFError as e:
        print(e)
    x = s.pop()
    print(f"First Pop -> {x}")
    x = s.pop()
    print(f"Second Pop -> {x}")
    x = s.pop()
    print(f"Third Pop -> {x}")
    try: 
        s.pop()
    except UFError as e:
        print(e)

def test_quque():
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Enqueue 1, 2, 3 -> {q}")
    try:
        q.enqueue(4)
    except OFError as e:
        print(e)
    x = q.dequeue()
    print(f"First Dequeue -> {x}")
    x = q.dequeue()
    print(f"Second Dequeue -> {x}")
    x = q.dequeue()
    print(f"Third Dequeue -> {x}")
    try: 
        q.dequeue()
    except UFError as e:
        print(e)

def test_hash_table():
    t = HashTable(10)
    t.insert(1, "a")
    t.insert(23, "hi")
    t.insert(55, "good")
    t.insert(55, "bad")
    print(t)
    print(f"Search key: 55 -> {t.search(55)}")
    try:
        t.search(44)
    except KeyError as e:
        print(e)

    delete_key = 55
    print(f"Delete Key: {delete_key}")
    t.delete(delete_key)
    print(t)
    try:
        t.delete(294)
    except KeyError as e:
        print(e)

def main():
    test_list()
    test_stack()
    test_quque()
    test_hash_table()

if __name__ == "__main__":
    main()