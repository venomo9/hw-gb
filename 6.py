def int_func (word):
    return word[0].upper() + word[1:]

list = []
str = input('введите строку: ')
word_list = str.split()
for word in word_list:
    list.append(int_func(word))

fin_str = ' '.join(list)
    
print(fin_str)
