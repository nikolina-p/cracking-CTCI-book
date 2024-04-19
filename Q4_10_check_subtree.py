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

    def is_subtree(self, t1: Node, t2: Node, r=None) -> bool:
        if r is None:
            # root of T2, if nodes do not match, we have to start over, checking from the root of T2 (TEST 2)
            r = t2

        if t1 is None and t2 is None:
            return True

        if not (t1 and t2):
            return False

        if t1.value == t2.value:
            return self.is_subtree(t1.left, t2.left, r) and self.is_subtree(t1.right, t2.right, r)
        else:
            return self.is_subtree(t1.left, r, r) or self.is_subtree(t1.right, r, r)


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
    a.left = Node("x")
    a.right = Node("y")
    f.left = t1a
    t1a.left = t1b
    #t1a.right = t1c

    tree_print(t1.root)

    t2 = BinaryTree(t2a)
    t2a.left = t2b
    t2a.right = t2c

    tree_print(t2.root)

    print(f"IS subtree (TEST 1): {t1.is_subtree(t1.root, t2.root)}")

    n1 = Node("A")
    n2 = Node("X")
    n3 = Node("B")
    n4 = Node("B")
    n5 = Node("D")
    n6 = Node("E")
    n7 = Node("D")
    n8 = Node("E")

    n1.left = n2
    n2.left = n3
    n2.right = n4
    n3.left = n5
    n3.right = n6
    n4.left = n7
    n4.right = n8

    s1 = Node("A")
    s2 = Node("B")
    s3 = Node("D")
    s4 = Node("E")

    s1.left = s2
    s2.left = s3
    s2.right = s4

    s_tree = BinaryTree(s1)
    n_tree = BinaryTree(n1)

    tree_print(n1)
    tree_print(s1)

    print(f"IS subtree (TEST 2): {n_tree.is_subtree(n_tree.root, s_tree.root)}")


r"""
OUTPUT:

                        d                       
           /                      \           
           e                      f           
     /          \          /          \     
     a          g          a          *     
  /    \    /    \    /    \    /    \  
  x    y    *    *    b    *    *    *  
    a    
  /    \  
  b    c  
IS subtree (TEST 1): False
                      A                      
           /                      \           
           X                      *           
     /          \          /          \     
     B          B          *          *     
  /    \    /    \    /    \    /    \  
  D    E    D    E    *    *    *    *  
           A           
     /          \     
     B          *     
  /    \    /    \  
  D    E    *    *  
IS subtree (TEST 2): False

"""
