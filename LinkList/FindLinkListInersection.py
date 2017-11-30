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
    

def findIntersect(linkList1, linkList2):
    l1 = getLinkLength(linkList1)
    l2 = getLinkLength(linkList2)
    shorter = linkList1 if l1 < l2 else linkList2
    longer = linkList2 if l1 < l2 else linkList1
    shorter = shorter.head
    print(longer)
    k = l1-l2
    longer = getKthNode(longer, k)

    print(longer.value)

    while (shorter != longer):
        shorter = shorter.nextnode
        longer = longer.nextnode

    return longer


def getKthNode(linkList, k):
    current = linkList.head
    while k >0 and current:
        current = current.nextnode
        k -= 1
    return current 

def getLinkLength(linkList):
    head = linkList.head
    counter = 0
    while head:
        counter += 1
        head = head.nextnode

    return counter


l = SingleLinkList()
l.add(1)
l.add(2)
l.add(1)
l.add(4)
l.add(2)

p = SingleLinkList()
p.add(1)
p.add(2)
p.add(1)

print(findIntersect(l, p))
