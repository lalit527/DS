from SingleLinkList import SingleLinkList

def checkCycle(LinkList):
    current = LinkList
    fast = LinkList
    while fast != None and fast.next != None:
        fast = fast.next.next
        current = current.next
        if current == fast:
            return True
    return False


sl = SingleLinkList()
sl.addToStart(1)
sl.addToStart(2)
sl.addToStart(3)
sl.addToEnd(4)
sl.addToEnd(5)
print(checkCycle(sl.getHead()))
