def count_letters(text):
	result = {}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] += 1
	return result
	
string = raw_input("enter value")
print(count_letters(string))
