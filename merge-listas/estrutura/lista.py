class ListNode:
    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

class List:
    def __init__(self):
        self.header = None
        self.nodesCounter = 0

    def insert(self, val):
        if val not in range(-100, 101):
            raise ValueError("Node value exceeded the maximum expected.")

        if self.nodesCounter >= 50:
            raise ValueError("List size exceeded the limit of 50 nodes.")

        node = ListNode(val)

        if self.header is None:
            self.header = node
        else:
            currNode = self.header

            while currNode.next:
                currNode = currNode.next

            currNode.next = node

        self.nodesCounter += 1
        
    def pop(self):
        if self.header is None:
            return None

        if self.header.next is None:
            node = self.header
            self.header = None
            self.nodesCounter -= 1
            return node

        current = self.header

        while current.next.next:
            current = current.next

        node = current.next
        current.next = None

        self.nodesCounter -= 1

        return node


                        

