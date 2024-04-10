"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.

From the book: A binary search tree is a binary tree in which every node fits a specific ordering property:
 all l e f t  descendents <= n < all  r i g h t descendents.
"""


class Node:
    def __init__(self, value:str):
        self.value = value
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value


def is_bst(root: Node, previous=None) -> bool:
    """do the inorder traversal: if each node is smaller than the previous, the tree is bst"""
    if not root:
        return True

    if not is_bst(root.left, previous):
        return False

    if previous and root < previous:
        return False

    previous = root

    return is_bst(root.right, previous)


if __name__ == '__main__':
    """
            18
           /   \ 
          10    20
         /    \    \ 
        5      13    25
              /   \
             11     15    
    """
    root = Node(18)
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(5)
    node_4 = Node(13)
    node_5 = Node(25)
    node_6 = Node(11)
    # node_7 = Node(15)
    node_7 = Node(19)

    root.left = node_1
    root.right = node_2
    node_1.left = node_3
    node_1.right = node_4
    node_2.right = node_5
    node_4.left = node_6
    node_4.right = node_7

    print(is_bst(root))
