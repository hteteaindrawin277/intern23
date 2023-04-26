class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert( root,key):
    if root is None:
        root=Node(key)
        return
    elif root.key==key:
        return
        if key<root.key:

          if key.left:insert(root.left,key)
            return
          root.left=Node(key)
          return

        if root.right:
            insert(root.right,key)
            return

          root.right=Node(key)

keys=list(map(int,input('enter data to compare').split()))
print(keys)
root=Node(keys[0])
for key in keys:
    insert(root,key)
