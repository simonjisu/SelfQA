
from typing import Any

class Node():
    def __init__(self, x: Any) -> None:
        self.data = x
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"

class SingleLinkedList():
    def __init__(self) -> None:
        r"""Single Linked List"""
        self.head = None

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
        return "SingleLinkedList"
        
    def insert(self, x: Any) -> None:
        r"""
        insert node to the front of list
        """
        n = Node(x)
        n.next = self.head
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
        t_prev = None
        while (t != None and t.data != x):
            t_prev = t
            t = t.next
        if (t != None):
            if t_prev != None:
                t_prev.next = t.next
            else:
                self.head = None

