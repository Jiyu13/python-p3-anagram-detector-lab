# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    
    def match(self, word_list):
        
        for word in word_list:
            
            if word == self.word:
                return word
            else:
                return []