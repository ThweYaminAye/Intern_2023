class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlinkedlist(self):
        result = self.head
        while result is not None:
            print(result.item)
            result = result.next

    def AtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def AtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def Inbetween(self, middle, data):
        if middle is None:
            print("Error")
            return
        newNode = Node(data)
        newNode.next = middle.next
        middle.next = newNode


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.head = Node(10)
    second = Node(20)
    third = Node(30)
    linkedlist.head.next = second
    second.next = third

    linkedlist.AtBeginning(100)
    linkedlist.Inbetween(linkedlist.head.next, 500)
    linkedlist.AtEnd(1000)

    # linkedlist.printlinkedlist()
    # print(linkedlist.head.item)
    while linkedlist.head is not None:
        print(linkedlist.head.item)
        linkedlist.head = linkedlist.head.next
