# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    
    def match(self, word_list):

        reversed = self.word[::-1]
        for word in word_list:
            if word == reversed:
                return word
            else:
                return []