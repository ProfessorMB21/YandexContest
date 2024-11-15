# create a binary tree
# traverse and create a tree
# perform three tree traversals
#   * In-order
#   * Post-order
#   * Pre-order

n = int(input().strip())

lst = [None for i in range(n)]

class Node:
    def __init__(self, value: int, left, right):
        self.value = value
        self.left = left
        self.right = right


def printInOrder(lst: list, node: Node):
    # a + b
    result = ""
    if node.left != -1:
        result += printInOrder(lst, lst[node.left])
    result += str(node.value) + ' '
    if node.right != -1:
        result += printInOrder(lst, lst[node.right])
    return result

def printPreOrder(lst: list, node: Node):
    # + a b
    result = ""
    result += str(node.value) + ' '
    if node.left != -1:
        result += printPreOrder(lst, lst[node.left])
    if node.right != -1:
        result += printPreOrder(lst, lst[node.right])
    return result

def printPostOrder(lst: list, node: Node):
    # a b +
    result = ""
    if node.left != -1:
        result += printPostOrder(lst, lst[node.left])
    if node.right != -1:
        result += printPostOrder(lst, lst[node.right])
    result += str(node.value) + ' '

    return result
    

for i in range(n):
    val, left, right = [int(x) for x in input().split()]
    lst[i] = Node(val, left, right)

print(printInOrder(lst, lst[0]))
print(printPreOrder(lst, lst[0]))
print(printPostOrder(lst, lst[0]))
