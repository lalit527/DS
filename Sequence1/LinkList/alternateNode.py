def alternateKNode(head, k):
    prevNode = None
    currNode = head
    nextNode = currNode.next
    
    while currNode != None:
        
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
        if nextNode != None:
            nextNode = nextNode.next
    head.head = prevNode
