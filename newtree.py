import bubblesort
class Node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
        self.link=None
        self.store=None
def tree_data():
    a=[]
    for i in range(97,123):
        a.append(chr(i))
    return a

def sec_tree_data():
    aa=[]
    for i in range(1,50):
        aa.append(i)
    return aa
def insert_tree_data(node:Node,data:list):
    if len(data)>0:
        mid=len(data)//2
        node.data=data[mid]
        if len(data[0:mid])>0:
            node.left=Node()
            insert_tree_data(node.left,data[0:mid])
        if len(data[mid+1:])>0:
            node.right=Node()
            insert_tree_data(node.right,data[mid+1:])
def printing(tree:Node):
    if tree:
        printing(tree.left)
        print(tree.data)
        printing(tree.right)
def create_tree():
    t_data=tree_data()
    print(t_data)
    tree=Node()
    insert_tree_data(tree,t_data)
    print(t_data)
    return tree
def create_sec_tree():
    t_data=sec_tree_data()
    print(t_data)
    tree=Node()
    insert_tree_data(tree,t_data)
    print(t_data)
    return tree


def insert_data(node: Node,name:str):
        if node.data==name[0]:
            if not node.link:
                node.link=create_sec_tree()
            insert_sec_data(node.link,name)
        elif node.data>name[0]:
            insert_data(node.left,name)
        else:
            insert_data(node.right,name)
def insert_sec_data(node:Node,name:str):
    if node.data==len(name):
        if not node.store:node.store=[]
        node.store.append(name)
    elif node.data<len(name):
        insert_sec_data(node.right,name)
    else:
        insert_sec_data(node.left,name)

def search_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link:return None
        return search_sec_data(node.link,name)
    elif node.data > name[0]:
        return search_data(node.left, name)
    else:
        return search_data(node.right, name)
def search_sec_data(node: Node, name: str):
    if node.data == len(name):
        if not node.store:return None
        print(node.store)
        return node.store[node.store.index(name)]
    elif node.data < len(name):
        return search_sec_data(node.right, name)
    else:
        return search_sec_data(node.left, name)
tree=create_tree()

#name=input('enter name:')
#insert_data(tree,name)
#printing(tree)
#name=input('please enter name:')
#insert_data(tree,name)
#printing(tree)
#name=input('enter rename')
#insert_data(tree,name)
#printing(tree)

name=input('enter name1:')
while name!='':
    insert_data(tree,name)
    name=input('Enter name2:')
name=input('Search name:')
print(search_data(tree,name))
