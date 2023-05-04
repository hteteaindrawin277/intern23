import random
import string
import json
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.link = None
        self.store = None
def tree_data():
    a = []
    for i in range(97, 123):
        a.append(chr(i))
    return a

def sec_tree_data():
    aa = []
    for i in range(1, 50):
        aa.append(i)
    #return aa
def insert_tree_data(node:Node,data:list):
    if len(data) > 0:
        mid = len(data)//2
        node.data = data[mid]
        if len(data[0:mid]) > 0:
            node.left = Node()
            insert_tree_data(node.left, data[0:mid])
        if len(data[mid+1:]) > 0:
            node.right = Node()
            insert_tree_data(node.right, data[mid+1:])
def printing(tree:Node):
    if tree:
        printing(tree.left)
        print(tree.data)
        printing(tree.right)
def create_tree():
    t_data = tree_data()
    #print(t_data)
    tree = Node()
    insert_tree_data(tree, t_data)
    #print(t_data)
    return tree
def create_sec_tree():
    sec_data = sec_tree_data()
    #print(t_data)
    tree = Node()
    insert_tree_data(tree, sec_data)
    #print(sec_data)
    return tree


def insert_data(node: Node, name: str):
    #print(node.data)
    #if not node: return
    if node.data == name[0]:
        if not node.link:
            node.link = create_sec_tree()
        insert_sec_data(node.link, name)
    elif node.data > name[0]:
        insert_data(node.left, name)
    else:
        insert_data(node.right, name)
def insert_sec_data(node: Node,name: str):
    #if not node : return
    if node.data == len(name):
        if not node.store:
            node.store = []
        idx = index(node.store, name)
        node.store = node.store[:idx] + [name] + node.store[idx:]
        #node.store.append(name)
    elif node.data < len(name):
        insert_sec_data(node.right, name)
    else:
        insert_sec_data(node.left, name)

def compare_str(str1, str2):
    for i in range(len(str2)):
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False
def index(arr: list, num):
    for i in range(len(arr)):
        if compare_str(arr[i], num):
            return i
    return len(arr)


def search_data(node: Node,name: str, ct):
    if node.data == name[0]:
        if not node.link:
            return None
        ct += 1
        return search_sec_data(node.link, name, ct)
    elif node.data > name[0]:
        ct += 1
        return search_data(node.left, name, ct)
    else:
        ct += 1
        return search_data(node.right, name, ct)
def search_sec_data(node: Node, name: str,ct):
    ct += 1
    if node.data == len(name):
        if not node.store:
            return None
        print(node.store)
        ct += 1
        return linear_search(node.store, name, ct)
        print(node.store)
        #return node.store[node.store.index(name)]
    elif node.data < len(name):
        ct += 1
        return search_sec_data(node.right, name, ct)
    else:
        ct += 1
        return search_sec_data(node.left, name, ct)
#tree=create_tree()
def linear_search(B, item, ct):
    i = 0

    while i != len(B):
        if B[i] == item:

            # return f"found in index {loc+i} "
            print('found at', end=' ')
            print(ct, 'times')
            return B[i]
        i += 1
    return 'not found'

#name=input('enter name:')
#insert_data(tree,name)
#printing(tree)
#name=input('please enter name:')
#insert_data(tree,name)
#printing(tree)
#name=input('enter rename')
#insert_data(tree,name)
#printing(tree)

'''name=input('enter name1:')
while name!='':
    insert_data(tree,name)
    name=input('Enter name2:')
name=input('Search name:')
print(search_data(tree,name)'''
'''import re
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, email):
        return True

    else:
        return False
def generator_email():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 20)))
    return f"{username}@gmail.com"
'''
total = []
if __name__ == '__main__':
    # first_tree = create_tree()

    with open('savedata.json') as f:
        data = json.load(f)
    fir_tree = create_tree()

    count = 10

    while count > 0:
        for i in range(10):
            email=data.get(f"{i}").get("email")
            insert_data(fir_tree, email)

            cot = 0
            search_data(fir_tree, email, cot)
            count = count - 1


    sum = 0
    for i in total:
        sum += i
    print('Average time=', sum / 1000)


