class Node:
    def __init__(self, data):
        self.data = None
        self.left = None
        self.right= None

def insertion(root_tree,total,email):
    result = 0
    if root_tree is None:
        return Node(email)
    for i in root_tree.data:
        result += ord(i)
    if total < result:
        root_tree.left = insertion(root_tree.left,total,email)
    else:
        root_tree.right = insertion(root_tree.right,total,email)
    return  root_tree

def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        #printing(node.right)
def testing(length,start):
    firstNode = ord(start)
    for i in range(length-1):
        firstNode += ord('m')
    return firstNode
tree = Node(5)



