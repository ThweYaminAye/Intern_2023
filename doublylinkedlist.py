class Node:
    def __init__(self, item):
        self.prev =  None
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


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    linkedlist.head.next = second
    second.prev = linkedlist
    second.next = third
    third.prev = second
    third.next = fourth
    #linkedlist.printlinkedlist()
    #print(linkedlist.head.item)
    while linkedlist.head is not None:
        print(linkedlist.head.item)
        linkedlist.head = linkedlist.head.next



