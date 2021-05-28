from typing import Any

class Node():
    def __init__(self, x: Any) -> None:
        self.data = x
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data}"

class CircularLinkedList():
    def __init__(self) -> None:
        r"""Circular Linked List"""
        self.nil = Node(None)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def __str__(self) -> str:
        if (self.nil.next == self.nil):
            return "[]"
        t = self.nil.next
        s = f"[{t}"
        while (t.next != self.nil):
            t = t.next
            s = s + f", {t}"
        return f"{s}]"
    
    def __name__(self) -> str:
        return "CircularLinkedList"
        
    def insert(self, x: Any) -> None:
        r"""
        insert node to the front of list
        """
        n = Node(x)
        n.next = self.nil.next
        self.nil.next.prev = n
        self.nil.next = n
        n.prev = self.nil
        
    def search(self, x: Any) -> bool:
        r"""
        search node if it exists
        """
        t = self.nil.next
        while (t != self.nil and t.data != x):
            t = t.next
        if (t != self.nil):
            return True
        return False
    
    def delete(self, x: Any) -> None:
        r"""
        delete node from the list
        """
        t = self.nil.next
        while (t != self.nil and t.data != x):
            t = t.next
        if (t != self.nil):
            t.prev.next = t.next
            t.next.prev = t.prev