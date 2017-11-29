class Node(object):

    def __init__(self, data):
        self.value = data
        self.nextnode = None

class SingleLinkList(object):
    def __init__(self):
        self.head = None
    
    def add( self, data ):
        node = Node(data)
        
        #return True
        if self.head == None:
           self.head = node 
        else:
            t = self.head
            while (t.nextnode != None):
                t = t.nextnode
            t.nextnode = node

    def deleteNode(self, data):
        temp = self.head
        prev = self.head
        if self.head == None:
            return 0

        while temp.value != data:
            prev = temp
            temp = temp.nextnode
        
        if temp.value == data:
            if temp == self.head:
                self.head = temp.nextnode
            prev.nextnode = temp.nextnode
    
    def reverseNode(self):
        temp = self.head
        previousNode = None
        nextNode = None

        while temp:
            #print(temp.value)
            nextNode = temp.nextnode
            temp.nextnode = previousNode

            previousNode = temp
            temp = nextNode
        self.head = previousNode
        
    def nthToLast(self, n):
        pass
       
    def printNode(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.nextnode   

    def deleteDup(self):
        buffer = []
        current = self.head
        previous = None
        while current:
            if current.value in buffer:
                previous.nextnode = current.nextnode
            else:
                buffer.append(current.value)
            previous = current
            current = current.nextnode
        print(buffer)
  

l = SingleLinkList()
l.add(1)
l.add(2)
l.add(1)
l.add(4)
l.add(2)
l.deleteDup()
#l.reverseNode()
l.printNode()
