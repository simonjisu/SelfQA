class kArrayNode():
    def __init__(self, x: int, k: int) -> None:
        self.val = x
        self.arity = k
        self.child = [None]*k
    
    def __str__(self):
        return f"N({self.val})"
    
    def __repr__(self):
        return self.__str__() + f": {[str(x) for x in self.child]}"

class BSTTravel():
    def __init__(self, root: kArrayNode=None):
        super().__init__()
        self.root = root
        
    def visit(self, curNode: kArrayNode):
        print(curNode)
        
    def BFT(self):
        """Breadth-First Traversal"""
        if self.root is None:
            return None
        # using queue
        q = [self.root]
        while q:
            curNode = q.pop(0)
            self.visit(curNode)
            for childNode in curNode.child:
                if childNode:
                    q.append(childNode)
                    
    def DFT(self, order: str="pre"):
        """Depth First Traversal"""
        if order == "pre":
            self._preorderDFT(self.root)
        elif order == "post":
            self._postorderDFT(self.root)
        elif order == "in":
            self._inorderDFT(self.root)
        
    def _preorderDFT(self, curNode: kArrayNode):
        if curNode is None:
            return None
        self.visit(curNode)
        for childNode in curNode.child:
            self._preorderDFT(childNode)
            
    def _postorderDFT(self, curNode: kArrayNode):
        if curNode is None:
            return None
        for childNode in curNode.child:
            self._postorderDFT(childNode)
        self.visit(curNode)
        
    def _inorderDFT(self, curNode: kArrayNode):
        # print(f"--> {curNode}")
        if curNode is None:
            return None
        if curNode.child:
            self._inorderDFT(curNode.child[0])
        self.visit(curNode)
        if curNode.child:
            self._inorderDFT(curNode.child[1])