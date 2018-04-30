from trees import Tree, Node
def isBST(root, left = None, right = None):
    if root is None:
        return True

    if left is not None and left.data >= root.data:
        return False
    
    if right is not None and right.data < root.data:
        return False

    return (isBST(root.left, left, root)
            and isBST(root.right, root, right))

t = Tree(5)
t.insertLeft(2)
t.insertRight(4)
root = t.getRoot()
t.inOrder(root)
print(isBST(root))