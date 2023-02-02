class BST:
    def __init__(self, parent, k):
        self.parent = parent
        self.key = k
        self.left = None
        self.right = None

    """Insert node into the BST"""

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                return self.left.insert(node)
        if node.key > self.key:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                return self.right.insert(node)

    """min value of tree of sub tree rooted at node"""

    def find_min(self):
        if self.left is None:
            return self.key
        else:
            return self.left.find_min()
    """finds & returns the node with the key k"""


    def find(self, k):
        if k == self.key:
            return self
        if k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        if k > self.key:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    """Returns the node with next largest key to self"""
    def next_larger(self):
        current = self.find(self.key)

        if current.right is not None:
            right_min = current.right.find_min()
            return current.find(right_min)

        elif current.parent is not None:
            while current is current.parent.right:
                current = current.parent
            return current.parent
        else:
            return "None: Single Node Tree"

    """Delete and returns the node from the  BST.
       If a key is passed, the find the node with the key, delete the node and then return the node"""
    def delete(self):
        """case 1: node to be deleted has no children + case 2: Has only one child"""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
            else:
                """self is self.parent.right"""
                self.parent.right = self.left or self.right
        else:
            """case 3: two children are present"""
            next_largest = self.next_larger()
            self.key, next_largest.key = next_largest.key, self.key
            next_largest.delete()




"""Prints the node in tree in low to high"""
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.key)
    inOrder(node.right)


if __name__ == "__main__":
    nodes_to_be_inserted = [52, 55, 53, 56, 37, 30, 42, 40, 41, 44]
    """RHS of Tree"""
    root = BST(None, 50)
    node1 = BST(root, 52)
    node2 = BST(node1, 55)
    node3 = BST(node2, 53)
    node4 = BST(node2, 56)
    """LHS of Tree"""
    node5 = BST(root, 37)
    node6 = BST(node5, 30)
    node7 = BST(node5, 42)
    node8 = BST(node7, 41)
    node9 = BST(node7, 44)
    node10 = BST(node8, 40)

    root.insert(node1)
    root.insert(node2)
    root.insert(node3)
    root.insert(node4)
    root.insert(node5)
    root.insert(node6)
    root.insert(node7)
    root.insert(node8)
    root.insert(node9)
    root.insert(node10)

    print("""print a node object- e.g. Node1""")
    print(node1)
    print("""print a node's key - e.g. Node1's key""")
    print(node1.key)
    print("Print ordered nodes in BST")
    inOrder(root)
    print("**** Min of a given node BST Tree ****")
    print(node2.find_min())
    print("**** find a node with search key ****")
    print(root.find(42).key)

    print("**** root key ****")
    print(root.key)
    print("**** find a node with next_larger key ****")
    print(node7.next_larger().key)

    print("****Delete a Node with a given key****")
    node7.delete()
    print("*** Print order of rooted node ***")
    print(node7.key)
    inOrder(node7)

