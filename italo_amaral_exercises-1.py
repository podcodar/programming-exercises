#1- Transforme uma lista de números com valores repetidos em uma lista com valores únicos.
#Obs1: a ordem da lista dos números retornados pode ser alatória.
#Obs2: use apenas as funções existentes no python para resolver o problema (não use set para resolver esse exercício).
print('Exercise 01:')
list_01 = [2,2,3,1,4,1]
list_02 = [1,2,3]
list_03 = [] 
def unique_values(normal_list):
    for i in normal_list:
        if normal_list.count(i) > 1:
            normal_list.remove(i)     
    return normal_list
print(unique_values(list_01))
print(unique_values(list_02))
print(unique_values(list_03))
print('')

#2- Conte a ocorrência de cada letra em uma dada palavra.
print('Exercise 02:')
ex1 = 'casa'
ex2 = 'azul'
ex3 = ''
def letter_count(word):
    counter = {}
    for letter in word:
        counter[letter] = 0
    for letter in word:
        if letter in counter.keys():
            counter[letter] += 1
    return counter
print(letter_count(ex1))
print(letter_count(ex2))
print(letter_count(ex3))
print('')

# 3- Data duas palavras, s1 e s2, retorne:
# -1 -> se s1 é lexicograficamente menor que s2
# 0 -> se s1 e s2 são identicas
# +1 -> se s1 é lexicograficamente maior que s2 """
print('Exercise 03:')
def lexographic_order(word_1, word_2):
    if word_1 < word_2:
        return -1
    elif word_1 > word_2:
        return 1
    else:
        return 0
print(lexographic_order('aaa', 'abc'))
print(lexographic_order('ccc', 'ccc'))
print(lexographic_order('zzz', 'aaa'))
print(lexographic_order('a', 'aa'))
print(lexographic_order('', 'a'))
print(lexographic_order('', ''))
