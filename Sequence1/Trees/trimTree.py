from binarytree import BinaryTree
def trimTree(root, minVal, maxVal):
    if root is None:
        return root

    root.left = trimTree(root.left, minVal, maxVal)
    root.right = trimTree(root.right, minVal, maxVal)

    if minVal <= root.data <= maxVal:
        return root

    if root.data > maxVal:
        return root.left

    if root.data < minVal:
        return root.right
    
    root.left()

bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)
# bt.inorder()
trimTree(bt.root, 30, 80)
bt.inorder()
