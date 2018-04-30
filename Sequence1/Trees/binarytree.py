class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def _insert(self, root, n):
        tmp = Node(n)
        if root is None:
            root = tmp
            return root
        if root.data < n:
            root.right = self._insert(root.right, n)
        else:
            root.left = self._insert(root.left, n)

        return root

    def insert(self, n):
        self.root = self._insert(self.root, n)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.data)
            self._inorder(root.right)

    def search(self, n):
        return self._search(self.root, n)

    def _search(self, root, n):
        if root:
            print(root.data)
        if root is None or root.data == n:
            return root
        if root.data > n:
            return self._search(root.left, n)
        else:
            return self._search(root.right, n)

    def delete(self, n):
        self._delete(self.root, n)

    def _successor(self, root):
            tmp = root.right
            while tmp.left is not None:
                tmp = tmp.left
            return tmp

    def _delete(self, root, n):
        if root is None:
            return root

        if n < root.data:
            root.left = self._delete(root.left, n)
        elif n > root.data:
            root.right = self._delete(root.right, n)
        else:
            if root.left is None:
                return root.right
                root = None
                return tmp
            elif root.right is None:
                return root.left
                root = None
                return tmp
            else:
                tmp = self._successor(root)
                root.data = tmp.data
                self._delete(root.right, tmp.data)

        return root