from typing import Any

class OFError(Exception):
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return f"OverFlow Error: at {self.x}"


class UFError(Exception):        
    def __str__(self):
        return f"UnderFlow Error: It's Empty"    
    

class Node():
    def __init__(self, x: Any) -> None:
        self.data = x
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data}"


class LinkedList():
    def __init__(self) -> None:
        r"""Linked List"""
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
    
    def insert_head(self, x: Any) -> None:
        r"""
        insert node to the front of list
        """
        n = Node(x)
        n.next = self.nil.next
        self.nil.next.prev = n
        self.nil.next = n
        n.prev = self.nil
        
    def insert_tail(self, x: Any) -> bool:
        r"""
        insert node to the end of list
        """
        n = Node(x)
        n.next = self.nil
        n.prev = self.nil.prev
        self.nil.prev.next = n
        self.nil.prev = n
    
    def delete_head(self) -> None:
        r"""
        delete node from the front of list
        """
        first = self.nil.next
        first.next.prev = self.nil
        self.nil.next = first.next
        return first.data


class Stack():
    def __init__(self, maximum:int) -> None:
        self.l = LinkedList()
        self.maximum = maximum
        self.count = 0
        
    def __str__(self) -> str:
        return str(self.l)
    
    def __len__(self):
        return self.count

    def __name__(self) -> str:
        return "Stack"

    def push(self, x: Any) -> None:
        if len(self) >= self.maximum:
            raise OFError(x)
        else:
            self.count += 1
            self.l.insert_head(x)
    
    def pop(self) -> Any:
        if len(self) == 0:
            raise UFError
        else:
            self.count -= 1
            return self.l.delete_head()


class Queue():
    def __init__(self, maximum:int) -> None:
        self.l = LinkedList()
        self.maximum = maximum
        self.count = 0
        
    def __str__(self) -> str:
        return str(self.l)
    
    def __len__(self):
        return self.count
    
    def __name__(self) -> str:
        return "Queue"

    def enqueue(self, x: Any) -> None:
        if len(self) >= self.maximum:
            raise OFError(x)
        else:
            self.count += 1
            self.l.insert_tail(x)
    
    def dequeue(self) -> Any:
        if len(self) == 0:
            raise UFError
        else:
            self.count -= 1
            return self.l.delete_head()