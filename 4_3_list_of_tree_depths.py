"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""


class TNode:
    """Tree node"""
    def __init__(self, name: str = None):
        self.name = name
        self.left = None
        self.right = None


class LNode:
    """Linkedlist node"""
    def __init__(self, value: str = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_node_values(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


def list_depths(root_node: TNode, parents=None, result=None) -> list:
    if not result:
        result = []

    llist = LinkedList()
    # parents - list that holds all TREE NODES that are on the same level; first level is root
    if not parents:
        parents = []
        l_node = LNode(root_node.name)
        llist.head = l_node
        parents.append(root_node)
    else:
        current_list_node = LNode()
        llist.head = current_list_node
        new_parents = []
        for t_node in parents:
            if t_node.left:
                if not current_list_node.value:  # if current is None
                    current_list_node.value = t_node.left.name
                else:
                    current_list_node.next = LNode(t_node.left.name)
                    current_list_node = current_list_node.next
                new_parents.append(t_node.left)
            if t_node.right:
                if not current_list_node.value:
                    current_list_node.value = t_node.right.name
                else:
                    current_list_node.next = LNode(t_node.right.name)
                    current_list_node = current_list_node.next
                new_parents.append(t_node.right)
        parents = new_parents

    # if "parents" on previous level have any children nodes, append the linked list to result and do recursion
    if llist.head.value:
        result.append(llist)
        list_depths(root_node, parents, result)

    return result


if __name__ == '__main__':
    """    
             A
            /
           B
         /   \
        C     D
               \
                E
    """
    node_a = TNode("A")
    node_b = TNode("B")
    node_c = TNode("C")
    node_d = TNode("D")
    node_e = TNode("E")

    node_a.left = node_b
    node_b.left = node_c
    node_b.right = node_d
    node_d.right = node_e

    result = list_depths(node_a)
    for linked_list in result:
        linked_list.print_node_values()
