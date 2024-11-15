# Huffman coding
# Restore a string by its code and prefix-free code of the characters
# first line contains two integers k and l separated by a whitespace
# 

class Node:
    def __init__(self, k, v, left, right):
        self.k = k
        self.v = v
        self.left = left
        self.right = right


k, l = map(int, input().split())
codes = {}

nodes = [None for i in range(k)]

for i in range(k):
    k, v = input().split(": ")
    codes[k.lower()] = v

def huffmanCoding(lst: list, node: Node):
    s = ""
    if node.left:
        s += huffmanCoding(lst, nodes[node.left])
    if node.right:
        s += huffmanCoding(lst, nodes[node.right])

    return s


for i in range(int(k)):
    print("dd")
    key, val = [x for x in input().split()]
    nodes[i] = Node(key, val)
    if not codes.__contains__(key):
        codes[key] = val

print(huffmanCoding(nodes))
print(codes)