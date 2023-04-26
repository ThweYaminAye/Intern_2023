class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def addNewNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printlinkedlist(self):
        result = self.head
        while result is not None:
            print(result.item)
            result = result.next


def getData():
    user = {}
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    birthday = input("Enter your birthday: ")
    budget = input("Enter your budget point")
    user.update({"name": name, "email": email, "password": password, "birthday": birthday, "budget": budget})
    return user


if __name__ == '__main__':
    linkedlist = Linkedlist()

    while 1:
        key = input('Press \'Y\' to continue.... Any other keys will exit!!!!')
        if key == 'Y' or key == 'y':


            userdata = getData()

            if linkedlist.head is None:
                linkedlist.head = Node(userdata)


            else:
                res = linkedlist.head
                while res is not None:
                    if res.item["email"] == userdata["email"]:
                        print("Your email is not unique..Please try again::::OK!")
                        break
                    res = res.next

                else:
                    linkedlist.addNewNode(userdata)
        else:
            break
    linkedlist.printlinkedlist()
