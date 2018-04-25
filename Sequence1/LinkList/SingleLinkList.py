class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToStart(self, n):
        tmp = self.head
        node = Node(n)
        self.head = node
        node.next = tmp
        if self.tail == None:
            self.tail = node

    def addToEnd(self, n):
        node = Node(n)
        self.tail.next = node
        self.tail = node

    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data)
            tmp = tmp.next

    def getHead(self):
        return self.head.data

    def getTail(self):
        return self.tail.data

sl = SingleLinkList()
sl.addToStart(1)
sl.addToStart(2)
sl.addToStart(3)
sl.addToEnd(4)
sl.addToEnd(5)
# print(sl.getHead())