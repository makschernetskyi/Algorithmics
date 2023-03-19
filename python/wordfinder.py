

import re


class Alphabet:
	def __init__(self, alphabet):
		self.alphabet = alphabet
		self.length = len(alphabet)
	def get_letters(self):
		return self.alphabet
	def get_length(self):
		return self.length



generated_words = []


russian_alphabet = Alphabet(['а','б','в','г','д','е','ё','ж','з','и','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'])


# def generate_possibles(alphabet, prefix, word_length):

# 	if word_length == 0:
# 		return generated_words.append(prefix)

# 	for letter in alphabet:
# 		new_prefix = prefix + letter
# 		generate_possibles(alphabet, new_prefix, word_length-1)





# generate_possibles(russian_alphabet.get_letters(), '', 6)

vocabulary = open('./voc.txt', mode='r', encoding='utf-8')


text = str(vocabulary.read())

words = re.findall(r"[\w']+", text)

def find_words():
	for word in words:
		if re.match(r"[а-яА-Я]+зор\b",word):
			generated_words.append(word)


find_words()



print("done!")

words_file = open('./words.txt', 'w')



try:
	words_file.write('\n'.join(generated_words))
finally:
	words_file.close()


