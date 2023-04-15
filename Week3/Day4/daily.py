# import string
# print(string.punctuation)
# # it's all punctuations what we can have
# class Text():
#
#  # def count_words():
#     # now this func delete all punctuations from file
#     def strip_punctuation(line):
#         for character in string.punctuation:
#             line = line.replace(character, "")
#         return line
#
#     filepath = "test.txt"
#
#     word_count = {}
#
#     with open(filepath, 'r') as fi:
#     # for every line in file
#         for line in fi:
#     #remove the punctuation
#             line = strip_punctuation(line)
#         # then seperated words and spaces
#             words = line.split()
#         # for each word in words
#             for word in words:
#             # convert into lowercase
#                 word = word.lower()
#                 if word not in word_count:
#                 # if not in - create new
#                     word_count[word] = 0
#                 else:
#                 # if in +1
#                     word_count[word] += 1
#
#                 wordsd = list(word_count.keys())
#                 for word in wordsd:
#                     print("{0:15}{1:8d}".format(word,word_count[word]))
#
#
#                 # for word in wordsd:
#                 #     print(word, word_count[word])
# This is too long way


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class Text():
# The "bonus part" is already implemented in the class initialization function
    def __init__(self, text_string) -> None:
        self.text_string = text_string
        self.origin_text_string = text_string
        for p in '.,?!":;\n()\\//♦—«-':
            self.text_string=self.text_string.replace(p,' ')
        self.text_string=self.text_string.split()
        for i,v in enumerate(self.text_string):
            self.text_string[i]=self.text_string[i].lower()
        # Used to remove stop words. But now it is disabled because this part takes a very long time.
        # self.text_string =[x for x in self.text_string if x not in stopwords.words()]
        self.text_string=" ".join(self.text_string)

    def frequency_in_text(self):
        dict_words={}
        for p in self.unique_words():
            dict_words[p]=self.text_string.count(p)
        dict_words={k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1])}
        return dict_words

    def most_common_word(self):
        word_dict=self.frequency_in_text()
        return (max(word_dict, key=word_dict.get))
        print(word)

    def unique_words(self):
        list_words=self.text_string.split(" ")
        return sorted(set(list_words))

#Exercise1
a=Text("A good book would sometimes, 'cost' as much as a good good good good good good house. A good book would sometimes, 'cost' as much as a good house.")
print("Frequency of words in text: \n",a.frequency_in_text())
print("Most frequent word: \n", a.most_common_word())
print("Unique words sorted in ascending order:\n", a.unique_words())

#Exercise2
with open("stranger.txt",'r') as f:
    all_text=f.read()
b=Text(all_text)
print("Frequency of words in text: \n",b.frequency_in_text())
print("Most frequent word: \n", b.most_common_word())
print("Unique words sorted in ascending order:\n", b.unique_words())
