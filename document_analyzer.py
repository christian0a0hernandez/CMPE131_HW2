def lex_sorter(file_name):
	file = open(file_name, 'r')
	print('\r')
	fr = file.read()
	word_array = fr.split()
	word_array.sort()
	word_count = {}

	for i in word_array:
		if (i in word_count.keys()):
			word_count[i] += 1
		else:
			word_count[i] = 1
	sorted_words = sorted(word_count, key = word_count.get, reverse = True)[:5]

	for i in sorted_words:
		print(i+":"+str(word_count[i]))

lex_sorter("document.txt")
