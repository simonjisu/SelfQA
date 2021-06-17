from typing import Any, Union

class TreeNode():
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val
        
    def __str__(self):
        return f"N({self.val})"
    
    def __repr__(self):
        return self.__str__()

class BST():
    def __init__(self, root: TreeNode=None):
        self.root = root
    
    def search(self, x: int) -> TreeNode:
        return self._search(x, self.root)
    
    def _search(self, x: int, curNode: TreeNode) -> TreeNode:
        if not curNode:  # if curNode is None = leaf node stop search
            return None
        if x == curNode.val:
            return curNode
        elif x < curNode.val:
            return self._search(x, curNode.left)
        else:
            return self._search(x, curNode.right)
    
    def insert(self, x: int) -> None:
        self.root = self._insert(x, self.root)
    
    def _insert(self, x: int, curNode: TreeNode) -> TreeNode:
        if curNode is None:  # if nothing in curNode insert x
            return TreeNode(x)
        if x == curNode.val:
            raise KeyError(f"Already have this {curNode}")
        elif x < curNode.val:
            curNode.left = self._insert(x, curNode.left)
        else:
            curNode.right = self._insert(x, curNode.right)
        
        return curNode
    
    def get_min(self, curNode=None) -> TreeNode:
        if curNode is None:
            curNode = self.root
        while curNode.left is not None:
            curNode = curNode.left
        return curNode
    
    def get_max(self, curNode=None) -> TreeNode:
        if curNode is None:
            curNode = self.root
        while curNode.right is not None:
            curNode = curNode.right
        return curNode
    
    def delete(self, x: int) -> None:
        self.root = self._delete(x, self.root)
    
    def _delete(self, x: int, curNode: TreeNode) -> Union[TreeNode, None]:
        # Case0: Empty Tree
        if curNode is None:
            return None
        if x < curNode.val:
            # parentNode.left = sub Tree 
            curNode.left = self._delete(x, curNode.left)
        elif x > curNode.val:
            # parentNode.right = sub Tree 
            curNode.right = self._delete(x, curNode.right)
        else:
            # Node founded
            # Case1: TreeNode with no children
            if curNode.left is None and curNode.right is None:
                return None
            # Case2: TreeNode with left child only
            elif curNode.left is not None and curNode.right is None:
                return curNode.left
            # Case3: TreeNode with right child only
            elif curNode.left is None and curNode.right is not None:
                return curNode.right
            # Case4: Root Node with two children
            else:
                # search maximun node from left tree
                leftNode = curNode.left
                leftParent = None
                while leftNode.right is not None:
                    leftParent = leftNode
                    leftNode = leftNode.right

                leftNode.right = curNode.right
                if leftParent is not None:
                    if leftNode.left is not None:
                        minNode = self.get_min(leftNode)
                        leftParent.right = None
                        minNode.left = leftParent
                    else:
                        leftParent.right = None
                        leftNode.left = leftParent

                return leftNode
                # otherwise:
                # search maximun node from right tree
                # rightNode = curNode.right
                # rightParent = None
                # while rightNode.left is not None:
                #     rightParent = rightNode
                #     rightNode = rightNode.left
                #     
                # rightNode.right = curNode.right
                # if rightParent is not None:
                #     if rightNode.right is not None:
                #     maxNode = self.get_max(rightNode)
                #     leftParent.left = None
                #     maxNode.right = maxParent
                # else:
                #     rightParent.left = None
                #     rightNode.right = rightParent
                # 
                # return rightNode
        return curNode