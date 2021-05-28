from typing import Any

class Node():
    def __init__(self, x: Any) -> None:
        self.data = x
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data}"

class DoublyLinkedList():
    def __init__(self) -> None:
        r"""Doubly Linked List"""
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        if (self.head == None):
            return "[]"
        s = f"[{self.head}"
        t = self.head.next
        while (t != None):
            s = s + f", {t}"
            t = t.next
        return f"{s}]"

    def __name__(self) -> str:
        return "DoublyLinkedList"
    
    def insert(self, x: Any) -> None:
        r"""
        insert node to the front of list
        """
        n = Node(x)
        n.next = self.head
        if (self.head != None):
            self.head.prev = n
        self.head = n
        
    def search(self, x: Any) -> bool:
        r"""
        search node if it exists
        """
        t = self.head
        while (t != None and t.data != x):
            t = t.next
        if (t != None):
            return True
        return False
    
    def delete(self, x: Any) -> None:
        r"""
        delete node from the list
        """
        t = self.head
        while (t != None and t.data != x):
            t = t.next
        if (t != None):
            if (t.prev != None):
                t.prev.next = t.next
            else:
                self.head = t.next
            if (t.next != None):
                t.next.prev = t.prev