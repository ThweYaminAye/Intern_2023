
class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right= None
    def insertion(self,data):
        if  self.data:
            if  self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertion(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertion(data)
        else:
            self.data = data
    def printing(self):
            if self.data is not None:
                if self.left:
                    self.left.printing()
                if self.right:
                    self.right.printing()
                print(self.data)

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
    tree.insertion(first[i])

for i in range(len(second)):
    tree.insertion(second[i])


# tree.printing()



