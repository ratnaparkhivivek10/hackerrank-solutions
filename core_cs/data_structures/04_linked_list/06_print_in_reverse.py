"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if(head is None):
        return
    else:
        data = []
        while(head is not None):
            data.append(head.data)
            head = head.next
        for item in reversed(data):
            print(item)
			
def ReversePrint(head):
    current = head
    if current:
        ReversePrint(current.next)
        print(current.data)
	
