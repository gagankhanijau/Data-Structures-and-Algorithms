

class Arraylist:
	def __init__(self):
		self.capacity=5
		self.length=0
		self.data=[None]*self.capacity

	def isEmpty(self):
		return True if self.length==0 else False

	def get(self, index):
		if self.length>index: 
			return self.data[index] 
		else:
			raise Exception('Index out of range')

	def set(self, value, index):
		if index>=self.length:
			self.data[index]= value	
		else:
			raise Exception('Index out of range')

	def add(self, value):
		if self.length+1 ==self.capacity:
			self.data+=([None]*self.length)	
		self.data[self.length]=value					
		self.length+=1
		self.capacity=len(self.data)

	def size(self):
		return self.length

	def print_list(self):
		print self.data, self.length, self.capacity	



list_obj= Arraylist()
list_obj.add(5)
list_obj.print_list()	
list_obj.add(4)
list_obj.print_list()
list_obj.add(3)
list_obj.print_list()
list_obj.add(2)	
list_obj.print_list()
list_obj.add(1)	
list_obj.print_list()
list_obj.add(0)
list_obj.print_list()
list_obj.add(-1)
list_obj.print_list()
list_obj.add(-2)
list_obj.print_list()
list_obj.add(-3)
list_obj.print_list()
list_obj.add(-4)
list_obj.print_list()
list_obj.add(-5)
list_obj.print_list()
list_obj.add(-6)
list_obj.print_list()
print  "Value at 5: ",list_obj.get(5)
list_obj.set(5,13)
list_obj.print_list()
#list_obj.get(20) #error		

