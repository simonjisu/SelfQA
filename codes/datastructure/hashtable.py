import math
from typing import Any

class Node():
    def __init__(self, key: int, value: Any) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return f"({self.key}, {self.value})"
    
class HashLinkedList():
    def __init__(self) -> None:
        self.nil = Node(None, None)
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
    
    def insert(self, key: int, value: Any) -> None:
        r"""
        insert (key, value) to the front of the list
        """
        n = Node(key, value)
        n.next = self.nil.next
        self.nil.next.prev = n
        self.nil.next = n
        n.prev = self.nil
        
    def search(self, key: int) -> Any:
        r"""
        search value of key
        """
        t = self.nil.next
        while (t != self.nil and t.key != key):
            t = t.next
            
        if (t != self.nil):
            return t
        return None
    
    def delete(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
        
class HashTable():
    def __init__(self, size: int):
        self.size = size
        self.t = [HashLinkedList() for i in range(size)]
        
    def __str__(self) -> str:
        s = "{\n"
        for i in range(self.size):
            s += f"{i}: {self.t[i]}, \n"
        return s + "}"
    
#     def h(self, key: Any) -> int:
#         r"""hash function"""
#         return key % self.size
    
    def h(self, key: int) -> int:
        r"""hash function2"""
        A = 0.16
        m = 8
        return math.floor(m * ((key * A) % 1))

    def __getitem__(self, key: int) -> HashLinkedList:
        return self.t[self.h(key)]
    
    def search(self, key: int) -> Any:
        x = self[key].search(key)
        if x is None:
            raise KeyError(f"Cannot find: {key}")
        return x
    
    def insert(self, key: int, value: Any) -> None:
        return self[key].insert(key, value)

    def delete(self, key: int) -> None:
        x = self.search(key)
        return self[key].delete(x)