class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

def insert(root,data):
    if root is None:
        root=Node(data)
    elif data<root.data:
        root.left=insert(root.left,data)
    elif data>root.data:
        root.right=insert(root.right,data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
root=Node('M')
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i  in letters:
    root=insert(root,i)
inorder(root)
