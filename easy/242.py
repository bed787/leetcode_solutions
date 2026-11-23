def str_to_hash(word):
	hash_table = {} 
	for letter in word:
		if letter not in hash_table:
			hash_table[letter] = 1
		else:
			hash_table[letter] += 1
	return hash_table

t = "abc"
s = "bcaa"
print(str_to_hash(s) == str_to_hash(t))


'''

Здесь просто по определению анаграммы идем. 
По сути, нам просто нужно подумать: "можно ли разобрать
каждое слово побуквенно и собрать второе"
Для этого достаточно разбить оба слова на хешмапы
в которых ключом будет буква, а значением будет количество этой буквы в слове

'''