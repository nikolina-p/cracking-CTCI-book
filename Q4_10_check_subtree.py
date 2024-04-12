"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1 .
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2,
That is, if you cut off the tree at node n, the two trees would be identical.
"""
from treeprint import tree_print


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def is_subtree(self, t1: Node, t2: Node) -> bool:
        if t1 is None and t2 is None:
            return True

        if not (t1 and t2):
            return False

        if t1.value == t2.value:
            return self.is_subtree(t1.left, t2.left) and self.is_subtree(t1.right, t2.right)
        else:
            return self.is_subtree(t1.left, t2) or self.is_subtree(t1.right, t2)


if __name__ == '__main__':
    t1a = Node('a')
    t1b = Node('b')
    t1c = Node('c')
    t2a = Node('a')
    t2b = Node('b')
    t2c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a = Node('a')
    b = Node('b')

    t1 = BinaryTree(d)
    d.left = e
    d.right = f
    e.left = a
    e.right = g
    a.left = b
    f.left = t1a
    t1a.left = t1b
    t1a.right = t1c

    tree_print(t1.root)

    t2 = BinaryTree(t2a)
    t2a.left = t2b
    t2a.right = t2c

    tree_print(t2.root)

    print(f"IS subtree: {t1.is_subtree(t1.root, t2.root)}")

"""
OUTPUT:

                         d                         
            /                        \            
            e                        f            
      /            \            /            \      
      *            *            a            *      
   /      \      /      \      /      \      /      \   
   *      *      *      *      b      c      *      *   
    a    
  /    \  
  b    c  
IS subtree: True

"""
