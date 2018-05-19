"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    previous = head
    current = head.next
    
    while current.next:
        if previous.data == current.data:
            previous.next = current.next
            
        previous = current.next    
        current = current.next.next
        
    return head