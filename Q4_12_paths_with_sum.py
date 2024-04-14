"""
4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

"""
from treeprint import tree_print
from collections import defaultdict
import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def paths_with_sum(node, target, current_sum=None, previous=None, counter=None) -> int:
    if node is None:
        return 0

    if not current_sum:
        current_sum = [0]

    if not previous:   # keeps track of previous sums on the current path
        previous = defaultdict(list)

    if not counter:
        counter = [0]

    current_sum[0] += node.value
    previous[current_sum[0]].append(True)

    if current_sum[0] == target:
        counter[0] += 1

    # check if on the current path, there are sums that are equal to (current_sum-target)
    if previous[current_sum[0] - target]:
        counter[0] += len(previous[current_sum[0]-target])

    if node.left:
        # pass the COPY of current_sum and previous so that recursion calls do not interfere with each other
        paths_with_sum(node.left, target, current_sum[:], copy.deepcopy(previous), counter)

    if node.right:
        paths_with_sum(node.right, target, current_sum[:], copy.deepcopy(previous), counter)

    return counter[0]


if __name__ == '__main__':
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(1)
    n6 = Node(2)
    n7 = Node(-2)
    n8 = Node(-3)
    n9 = Node(11)

    n1.left = n2
    n2.left = n3
    n3.left = n4
    n2.right = n5
    n5.right = n6
    n3.right = n7
    n1.right = n8
    n8.right = n9

    tree_print(n1)

    no_of_paths = paths_with_sum(n1, 8)
    print(f"Number of paths is: {no_of_paths}")

    k1 = Node(2)
    k2 = Node(3)
    k3 = Node(-3)
    k4 = Node(4)
    k5 = Node(1)
    k6 = Node(2)
    k7 = Node(-2)
    k8 = Node(4)
    k9 = Node(4)
    k10 = Node(6)

    k1.left = k2
    k1.right = k3
    k2.left = k4
    k2.right = k5
    k3.right = k6
    k4.left = k7
    k5.right = k8
    k6.left = k9
    k6.right = k10

    tree_print(k1)

    no_of_paths = paths_with_sum(k1, 5)
    print(f"Number of paths is: {no_of_paths}")

"""
OUTPUT book test case:
                        10                        
            /                        \            
            5                        -3            
      /            \            /            \      
      3            1            *            11      
   /      \      /      \      /      \      /      \   
   3      -2      *      2      *      *      *      *   
Number of paths is: 3

OUTPUT:
                      2                      
           /                      \           
           3                      -3           
     /          \          /          \     
     4          1          *          2     
  /    \    /    \    /    \    /    \  
  -2    *    *    4    *    *    4    6  
Number of paths is: 5

"""
