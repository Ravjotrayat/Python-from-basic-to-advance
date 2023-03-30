#inorder=Left Root Right
#preorder= Root Left Right
#postorder=Left Right Root
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item

#Basic operations on Binary Tree(inorder,preorder and postorder)
def inorder(root):
        if root:
            inorder(root.left)
            print(str(root.val)+"->",end='')
            inorder(root.right)
def preorder(root):
        if root :
            print(str(root.val)+"->",end='')
            preorder(root.left)
            preorder(root.right)
def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(str(root.val)+"->",end='')

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Inorder traversal")
inorder(root)
print()
print("\nPreorder traversal")
preorder(root)
print()
print("\nPostorder traversal")
postorder(root)

