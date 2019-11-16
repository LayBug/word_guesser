from itertools import permutations
def dictwords():
	with open('words_alpha.txt directory', 'r') as words:
		words_set = list(words)
	return words_set
	
dictionary= dictwords()
		
def permutate(word, n):
	permutated_list = [''.join(x) for x in permutations(word, n)]
	return permutated_list

def match():
	word = input("Please enter word: ").lower()
	n = int(input("Enter word length: "))
	global dictionary
	matched = []
	permutated_list= permutate(word, n)
	for i in permutated_list:
		i = i + '\n'
		if i in  dictionary:
			length = len(i)-1
			matched.append(i[:length])
	for i in matched:
		print(i)

match()

