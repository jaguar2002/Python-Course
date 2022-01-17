def highlight_word(sentence, word): 
	words_in_sentence = sentence.split()
	new_sentence = " "
	
	for word_ in words_in_sentence:
		if(word_ == word):
			index = words_in_sentence.index(word_)
			capitilized_word = word_.upper()
			words_in_sentence.remove(word_)

			words_in_sentence.insert(index,capitilized_word)
	

	new_sentence = " ".join(words_in_sentence)

	return(new_sentence)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud!"))
print(highlight_word("Automating with Python is fun", "fun"))
