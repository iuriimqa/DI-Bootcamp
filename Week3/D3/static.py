class Useful:

    @staticmethod
    def capitalize_word(word:str):
        return word.capitalize()
    
    @staticmethod
    def multiply_by_19(number:int):
        return number * 19
    

w = Useful.capitalize_word('word')
print(w)

n = Useful.multiply_by_19(10)
print(n)
