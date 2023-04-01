# sample = input("Input words with coma and space between")
# a = input("input words with space between?")
# a= a.split()
# alist= list(a)
# alist = sorted(alist)
# b = str(alist)
# print(b)

def sorted_func(word_list: str):
    for i, word in enumerate(word_list):
        word_list[i] = word_list.strip(' ')
    return sorted(word_list)

words= input("please input words with coma")
words_list = words.split(',')

res = sorted_func(words_list)