import tree
import second_tree
fir_tree = tree.tree
sec_tree = second_tree.tree
class newNode:
    def __init__(self, data):
        self.data = []
        self.left = None
        self.right= None
def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)


def connection_test(ftree,name):
    if ftree is not None:
        connection_test(ftree.left,name)
        if ftree.data == name[0]:
            sec_tree_connection_test(sec_tree,len(name),name)
            return
        connection_test(ftree.right,name)

def sec_tree_connection_test(sec_tree,length,username):
    if sec_tree is not None:
        sec_tree_connection_test(sec_tree.left,length,username)
        if sec_tree.data == length:
            sec_tree.sec_data.append(username)
            sec_tree.sec_data = sortedList(sec_tree.sec_data)
            print(sec_tree.sec_data)
            # result = sortedList(sec_tree.sec_data)
            # newNode.data = result
            # print(newNode.data)
            return
        sec_tree_connection_test(sec_tree.right,length,username)


#comparison countin sort
def sortedList(list):

    counting = []
    S = []
    for i in range(len(list)):
        counting.append(0)
    for i in range(len(list)):
        S.append(0)
    for i in range(len(list)):
        for j in range (i+1,len(list)):
            if changeAscii(list[i]) > changeAscii(list[j]):
                counting[i] += 1
            elif changeAscii(list[i]) < changeAscii(list[j]):
                counting[j] += 1
    for i in range(len(list)):
        S[counting[i]] = list[i]
    return S
def changeAscii(char):
    total = 0
    for i in char:
        total += ord(i)
    return total

# def sendData():
#     return newNode

def emailSplit(email):
    res = []
    update = ''
    for i in email:
        res += i
    for i in range(len(res) - 10):
        update += res[i]
    return update
def sec_tree_connection(sec_tree,userEmail):
    if sec_tree is not None:
        sec_tree_connection(sec_tree.left,userEmail)
        if sec_tree.data == len(userEmail):
            print("Checking",sec_tree.sec_data)
            newNode.data = sec_tree.sec_data
            return
        sec_tree_connection(sec_tree.right,userEmail)
def binarySearchAlgo(list,item):
    first = 0
    last = len(list)-1
    index = -1

    while first <= last and index == -1:
        mid = (first+last)//2
        if list[mid] == item:
            index = mid
        else:
            if list[mid] > item:
                last = mid-1
            else:
                first = mid+1
    return index
# list = [10,20,30,40,50,60,70]
# result = binarySearchAlgo(list,60)
secondResult = []
if __name__ == '__main__':
    con = True
    while con:
        name = input("Enter your email...")
        test = input ("Enter 'z' or 'Z' key to exit.....")
        if test == 'z' or test == 'Z':
            con = False
        else:
            updateName = emailSplit(name)
            connection_test(fir_tree,updateName)

    item = input("Enter search item")
    updateItem = emailSplit(item)
    sec_tree_connection(sec_tree,updateItem)
    ind = binarySearchAlgo(newNode.data,updateItem)
    if ind >= 0:
        print("Finding at index",ind)
        newNode.data[ind]+='@gmail.com'
        print(newNode.data[ind])
    else:
        print("Finding at index", ind)
        print("Your email doesn't exist")









