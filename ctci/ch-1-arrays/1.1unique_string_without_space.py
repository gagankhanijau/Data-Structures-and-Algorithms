
def check_uniqueness(string):
	bitmap=0
	string=string.upper()
	for char in string:
		bit_index=ord(char)-48
		if bitmap & (1<<bit_index):
			return False
		bitmap= bitmap| (1<<bit_index)
	return True		


print check_uniqueness('abcdef3g')			
print check_uniqueness('abcdeafg')