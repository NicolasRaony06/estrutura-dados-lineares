from estrutura.lista import List, ListNode

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return head
        

list1 = List()
list1.insert(1)
list1.insert(2)
list1.insert(4)

list2 = List()
list2.insert(1)
list2.insert(3)
list2.insert(4)

list3 = List()
list3.header = merge_two_lists(list1.header, list2.header)

node = list3.header
while node:
    print(node.val)
    node = node.next