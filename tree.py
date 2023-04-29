# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

def insertion(alpha,root_tree):
    if root_tree is None:
        return Node(alpha)
    if ord(alpha) < ord(root_tree.data):
        root_tree.left = insertion(alpha,root_tree.left)
    else:
        root_tree.right = insertion(alpha,root_tree.right)
    return  root_tree

def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        #printing(node.right)

main_tree = []
for i in range(97,123):
    main_tree.append(chr(i))

length = len(main_tree)
mid = length//2
tree = Node('m')
first = main_tree[0:mid-1]
second = main_tree[mid:length]
first.reverse()
for i in range(len(first)):
    tree = insertion(first[i],tree)

for i in range(len(second)):
    tree = insertion(second[i], tree)
printing(tree)


