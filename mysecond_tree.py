class Node:
    def __init__(self, data):
        store = {}
        for i in range(97,123):
            store[chr(i)] = []
        self.data = data
        self.sec_data = store
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
                print(self.data)
                if self.right:
                    self.right.printing()


main_tree = []
for i in range(26):
    main_tree.append(i)

length = len(main_tree)
mid = length//2
tree = Node(13)
first = main_tree[0:mid]
second = main_tree[mid+1:length]
# first.reverse()
for i in range(len(first)):
    tree.insertion(first[i])

for i in range(len(second)):
    tree.insertion(second[i])


# tree.printing()



