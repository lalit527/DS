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

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.nextnode        
  

l = SingleLinkList()
l.add(1)
l.add(2)
l.add(3)
l.printNode()
