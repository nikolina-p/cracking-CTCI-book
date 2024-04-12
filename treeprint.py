"""
tree_print(node: Node) - function prints the binary tree structure under the given node
in_level_traversal(node: Node) - function returns a list of tree levels, where tree level
                                is a list of nodes in the current level
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def in_level_traversal(root, all_nodes: list = None, parents: list = None) -> list:
    """
    return list of levels, where level is a list containing nodes in that level;
    Nonexistent child is replaced with '-' sign for printing purposes
    """
    if parents is None:
        parents = [root]

    if all_nodes is None:
        all_nodes = [parents]

    _ = []
    for parent in parents:
        if parent:
            if parent.left:
                _.append(parent.left)
            else:
                _.append(None)
            if parent.right:
                _.append(parent.right)
            else:
                _.append(None)
        else:
            _ += [None, None]
    parents = _

    if any(item is not None for item in parents):
        all_nodes.append(parents)
        in_level_traversal(root, all_nodes, parents)

    return all_nodes


def tree_print(root) -> None:
    """
    function prints binary tree/subtree that is covered by the given node
    !!! the class of the node has to implement __str__ method
    """
    levels = in_level_traversal(root)
    width = len(levels[-1]) * 3 + sum([len(str(item)) for item in levels[-1]])

    result_str = []

    for level in levels:
        item_width = int(width/len(level))   # string "space" for each element
        empty_space = " " * (item_width // 2)
        level_str = edges = ""
        open_parenthesis = 1
        for item in level:
            m = len(str(item)) if item else 1    # get number of characters in node value
            x = -m//2 if m > 1 else None
            level_str += empty_space + (str(item) if item else "*") + empty_space
            edges += empty_space + ("/" if open_parenthesis % 2 == 1 else "\\") + empty_space
            open_parenthesis += 1
        if len(level) > 1:
            print(edges)
        print(f"{level_str}")
        result_str.append(level_str)


if __name__ == '__main__':
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

    tree_print(node_a)
