unique = {}

for index, letter in enumerate(s):
	if letter not in unique:
		unique[letter] = index
	else:
		unique[letter] = -1

result = -1

for letter in s:
	if unique[letter] != -1:
		result = unique[letter]
		break

print(result)

'''
Для этой задачи в первую очередь в голову пришла идея о
создании хешмапы, где ключом будет выступать символ,
а значением либо (-1), если символ не уникален,
либо его индекс

По времени O(n + k), где n - колво элементов в s,
а k - первый индекс первого уникального элемента.
По памяти будет O(d), где d - колво уникальных элментов 
в строке s, но т.к. по условию там ток английск
строчный то по сути это O(1)

'''