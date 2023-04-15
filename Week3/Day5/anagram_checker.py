class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt', 'r') as f:
            self.word_list = [line.strip() for line in f]

    def is_valid_word(self, word):
        return word in self.word_list

    def is_anagram(self, word1, word2):
        return set(word1.lower()) == set(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams
