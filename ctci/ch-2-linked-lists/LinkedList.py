
class Node:
	def __init__(self, value):
		self.value = value
		self.next=None
		self.prev=None

	def set_data(self, value):
		self.value=value

	def get_data(self):
		return self.value

	
class LinkedList:
	def __init__(self, is_doubly=False):
		self.is_doubly=is_doubly
		self.head=None

	def add(self, value):
		new_node=Node(value)
		if head is None: 
			head=new_node
		else:
			temp=head
			while temp.next is not None:
				temp=temp.next
			temp.next=new_node
			if is_doubly:
				new_node.prev=temp

	# returns head of the linked list
	def delete(self, value):
		temp=head
		if temp is not None:
			if temp.value==value:
				return temp.next
			else:
				while temp.next is not None:
					if temp.next.value==value:
						temp.next= temp.next.next
						return head
					temp= temp.next		
		else:
			return temp					