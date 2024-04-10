"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""


class Node:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None


def get_height(root: Node) -> bool:
    if not root:
        return 0

    if not root.left and not root.right:
        return 0

    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root: Node) -> bool:
    return not abs(get_height(root.left) - get_height(root.right)) > 1


if __name__ == '__main__':
    """
               A
            /     \
           B       E
         /   \
        C     D
          \
           F
    """

    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    node_a.left = node_b
    node_a.right = node_e
    node_b.left = node_c
    node_b.right = node_d
    node_c.right = node_f

    print("IS BALANCED? ", is_balanced(node_a))
