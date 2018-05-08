"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    equal = 1
    while(headA and headB):
        if (headA.data != headB.data) or ((headA.next is None and headB.next) or (headA.next and headB.next is None)):
            equal = 0
            break
        headA = headA.next
        headB = headB.next
        
    return equal

    if headA is None and headB is None:
        return 1
    if( (headA is None and headB) or (headA and headB is None) ):
        return 0
  