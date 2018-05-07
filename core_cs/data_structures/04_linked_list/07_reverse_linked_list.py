"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if(head is None):
        return
    else:
        original = []
        while(head is not None):
            original.append(head)
            head = head.next
        original.reverse()
        original.append(None)
        count = 0
        for node in original:
            if(node is not None):
                node.next = original[count+1]
                count = count + 1
        return original[0]
