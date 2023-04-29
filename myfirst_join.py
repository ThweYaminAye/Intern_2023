import myfirst_tree
import mysecond_tree
from myfirst_tree import Node

first_tree: Node = myfirst_tree.tree
second_tree = mysecond_tree.tree
list = []
for i in range(97,123):
    list.append(chr(i))

def connection_test(first_tree,email):
    if first_tree is not None:
        connection_test(first_tree.left,email)
        if first_tree.data == email[0]:
            second_connection(second_tree,email,len(email))
            return
        connection_test(first_tree.right,email)

def second_connection(second_tree,email,length):
    result = []
    if second_tree is not None:
        second_connection(second_tree.left,email,length)

        if second_tree.data == length :
            second_tree.sec_data[email[0]].append(email)
            second_tree.sec_data[email[0]] = sortedList(second_tree.sec_data[email[0]])
            print(second_tree.sec_data[email[0]])
            return

        second_connection(second_tree.right,email,length)

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

def printing(node):
    if node is not None:
        printing(node.left)
        if node.sec_data is not None:
            print(node.sec_data)
        printing(node.right)

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


def emailSplit(email):
    res = []
    update = ''
    for i in email:
        res += i
    for i in range(len(res) - 10):
        update += res[i]
    return update

def checkEmail_connection(second_tree,email):
    if second_tree is not None:
        checkEmail_connection(second_tree.left,email)
        if (second_tree.data == len(email)):
            find = binarySearchAlgo(second_tree.sec_data[email[0]],email)
            if find >= 0:
                print("We found")
            else:
                print("Not found")
            return
        checkEmail_connection(second_tree.right, email)













if __name__ == '__main__':
    for i in range(5):
        email = input("Enter your email")
        k,l,m= 0,0,0
        if len(email) <= 40 and len(email) > 10 :
            if email[0].isalpha():
                if ('@' in email) and email.count('@') == 1:
                    if (email[-4] == '.') or (email[-3] == '.'):
                        for i in email:
                            if i.isspace():
                                k = 1
                            elif i.isalpha():
                                if i.isupper():
                                    l = 1
                            elif i.isdigit():
                                continue
                            elif i == '_' or i == '.' or i == '@':
                                continue
                            else:
                                m = 1
                        if k == 1 or l == 1 or m == 1 :
                            print("Your Email is not valid ")
                        else:
                            storeEmail = emailSplit(email)
                            connection_test(first_tree, storeEmail)
                    else:
                        print("Your Email is not valid")
                else:
                    print("Your Email is not valid")
            else:
                print("Your Email is not valid")
        else:
            print("Your Email is not valid")




    checkEmail = input("Enter your email to check exist or not!")
    updateCheckEmail = emailSplit(checkEmail)
    checkEmail_connection(second_tree,updateCheckEmail)

    printing(second_tree)