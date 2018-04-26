class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFront(self, n):
        node = Node(n)
        tmp = self.head
        if tmp == None:
            self.head = node
            self.tail = node
        else:
            self.head = node
            tmp.prev = node
            node.next = tmp

    def insertEnd(self, n):
        node = Node(n)
        tmp = self.tail
        if tmp == None:
            self.head = node
            self.tail = node
        else:
            self.tail = node
            tmp.next = node
            node.prev = tmp

    def printElement(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data)
            tmp = tmp.next

    def printElementP(self):
        tmp = self.tail
        while tmp != None:
            print(tmp.data)
            tmp = tmp.prev

dl = DoubleLinkList()
dl.insertEnd(1)
dl.insertEnd(2)
dl.insertEnd(3)
dl.printElementP()