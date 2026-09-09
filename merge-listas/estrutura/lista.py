class ListNode:
    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

class List:
    def __init__(self):
        self.header = None
        self.nodesCounter = 0

    def insert(self, val):
        if not val in range(-100, 101):
            raise ValueError("Node Value exceded the maximun expected.")

        if not self.nodesCounter <= 50:
            raise ValueError("List size exceded the limit of 50 nodes.")

        node = ListNode(val)
        if not self.header:
            self.header = node
            self.nodesCounter += 1
            return

        currNode = self.header
        while currNode:
            if not currNode.next:
                currNode.next = node
                self.nodesCounter += 1
                break
            currNode = currNode.next

    def pop(self):
        node = self.header
        while node:
            if not node.next.next:
                node.next = None
                self.nodesCounter -= 1
                break
            node = node.next


                    

