from SingleLinkList import SingleLinkList

def reverseList(List):
    prevNode = None
    currNode = List.getHead()
    nextNode = currNode.next
    
    while currNode != None:
        
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
        if nextNode != None:
            nextNode = nextNode.next
    List.head = prevNode

    tmp = prevNode
    # while tmp != None:
    #     print("current", tmp.data)
    #     tmp = tmp.next
    


sl = SingleLinkList()
sl.addToStart(1)
sl.addToStart(2)
sl.addToStart(3)
sl.addToEnd(4)
sl.addToEnd(5)
reverseList(sl)
sl.printList()
