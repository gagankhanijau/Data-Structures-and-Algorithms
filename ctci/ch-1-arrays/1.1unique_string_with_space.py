
def check_uniqueness(string):
	char_hash_map = dict()
	for char in string:
		if char_hash_map.get(char, None) is not None:
			return False
		char_hash_map[char]=1
	return True


print check_uniqueness('abcdefg')			
print check_uniqueness('abcdeafg')