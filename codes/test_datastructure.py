from datastructure import SingleLinkedList, DoublyLinkedList, CircularLinkedList, Stack, Queue, HashTable, BST, TreeNode
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

def test_bst():
    # check insert, search, delete
    def get_tree(insert_12=False):
        r"""
                4
              /   \
             2    10
           /  \  /  \
          1   3 8   12
                /
                6
                \
                7
        """
        bst = BST(root=TreeNode(4))
        bst.root.left = TreeNode(2)
        bst.root.left.left = TreeNode(1)
        bst.root.left.right = TreeNode(3)
        bst.root.right = TreeNode(10)
        bst.root.right.left = TreeNode(8)
        bst.root.right.left.left = TreeNode(6)
        bst.root.right.left.left.right = TreeNode(7)
        if insert_12:
            bst.root.right.right = TreeNode(12)
        return bst

    bst = get_tree(insert_12=False)
    # search
    search8 = bst.search(8)
    assert search8.val == 8
    # insert
    bst.insert(12)
    search12 = bst.search(12)
    assert search12 == bst.root.right.right
    # max
    maxNode = bst.get_max()
    assert maxNode.val == 12
    # min
    minNode = bst.get_min()
    assert minNode.val == 1
    # delete leaf node
    bst.delete(3)
    search3 = bst.search(3)
    assert search3 == bst.root.left.right
    # delete node with child
    bst = get_tree(insert_12=True)
    bst.delete(6)
    search7 = bst.search(7)
    assert search7 == bst.root.right.left.left
    # delete node with both child
    bst = get_tree(insert_12=True)
    bst.delete(10)
    search7 = bst.search(7)
    assert search7 == bst.root.right.left.right
    search12 = bst.search(12)
    assert search12 == bst.root.right.right
    # delete root node
    bst = get_tree(insert_12=True)
    bst.delete(4)
    search3 = bst.search(3)
    assert search3 == bst.root
    search1 = bst.search(1)
    assert search1 == bst.root.left.left
    search7 = bst.search(7)
    assert search7 == bst.root.right.left.left.right
    print("all bst test passed")

def main():
    # TODO: Change all test to unittest code
    test_list()
    test_stack()
    test_quque()
    test_hash_table()
    test_bst()

if __name__ == "__main__":
    
    main()