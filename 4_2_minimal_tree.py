class Node:

    def __init__(self, value: int = None, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, root: Node = None):
        self.root = root

    def tree_print(self):
        levels = self.in_level_traversal()
        for level in levels:
            print([node.value if isinstance(node, Node) else node for node in level])  # last level can contain str '-'

    def in_level_traversal(self, all_nodes: list = None, parents: list = None) -> list:
        """return list of levels, where level is a list containing nodes in that level;
        Nonexistent child is replaced with '-' sign for printing purposes"""
        if parents is None:
            parents = [self.root]

        if all_nodes is None:
            all_nodes = [parents]

        _ = []
        for parent in parents:
            if isinstance(parent, Node):
                if parent.left:
                    _.append(parent.left)
                else:
                    _.append("-")
                if parent.right:
                    _.append(parent.right)
                else:
                    _.append("-")
            else:
                _ += ['-', '-']
        parents = _

        if any(isinstance(item, Node) for item in parents):
            all_nodes.append(parents)
            self.in_level_traversal(all_nodes, parents)

        return all_nodes

    def __str__(self):
        return str(self.root.value)


def build_min_height_bst(arr: list):
    """Q.4_2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
    to create a binary search tree with minimal height."""

    if len(arr) == 0:
        return None

    x = len(arr) // 2

    root = Node(arr[x])

    if len(arr) > 1:
        """there is one or more to the left"""
        root.left = build_min_height_bst(arr[:x]) if len(arr[:x]) > 1 else Node(arr[x-1])
    if len(arr) > x + 1:
        """there is one or more to the right"""
        root.right = build_min_height_bst(arr[x+1:]) if len(arr[x+1:]) > 1 else Node(arr[x+1])

    return root


def build_complete_bst(arr: list) -> Node:
    """Q.4_2 Variation - COMPLETE tree: Given a sorted (increasing order) array with unique integer elements,
    write an algorithm to create a COMPLETE binary search tree."""

    """Idea: Calculate the number of elements that will go to the right branch of the tree. Since the array is sorted,
    that will be the index of the root element. Do the recursion to get 'root' elements of subtrees"""

    if not arr:
        return None

    if len(arr) == 1:
        return Node(arr[0])

    levels = 1
    nodes_in_level = 1
    total_full = 1

    while total_full < len(arr):
        levels += 1
        nodes_in_level = nodes_in_level * 2
        total_full += nodes_in_level

    diff_to_full = total_full - len(arr)   # how many elements we lack to have full last level

    leaves = nodes_in_level - diff_to_full  # how many leaves we will have (the bottom level)
    full_tree = total_full - nodes_in_level  # how many nodes total will go into the levels above the bottom level

    # calculate number of elements of the array that will be put in left side of the tree
    index = int((full_tree - 1) / 2 + min(leaves, nodes_in_level/2))

    root = Node(arr[index])

    if len(arr) > 1:
        # there is one or more to the left
        root.left = build_complete_bst(arr[:index]) if index > 1 else Node(arr[index-1])
    if len(arr) > index + 1:
        # there is one or more to the right
        root.right = build_complete_bst(arr[index+1:]) if len(arr[index+1:]) > 1 else Node(arr[index+1])

    return root


if __name__ == '__main__':

    test_cases = [
        [],
        range(1,8),
        range(0, 18),
        [1]
    ]

    for test in test_cases:
        print("Test: ",list(test))
        my_tree = BST(build_min_height_bst(test))
        my_tree.tree_print()
        print("\n")

    test = range(1, 11)
    complete_tree = BST(build_complete_bst(test))
    print("COMPLETE TREE: ", list(test))
    complete_tree.tree_print()

    """
    OUTPUT:
    Test:  []
    [None]
    
    
    Test:  [1, 2, 3, 4, 5, 6, 7]
    [4]
    [2, 6]
    [1, 3, 5, 7]
    
    
    Test:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    [9]
    [4, 14]
    [2, 7, 12, 16]
    [1, 3, 6, 8, 11, 13, 15, 17]
    [0, '-', '-', '-', 5, '-', '-', '-', 10, '-', '-', '-', '-', '-', '-', '-']
    
    
    Test:  [1]
    [1]
    
    
    COMPLETE TREE:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [7]
    [4, 9]
    [2, 6, 8, 10]
    [1, 3, 5, '-', '-', '-', '-', '-']
    """
