# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    
    def match(self, word_list):

        matched_words = []
        given_word_letters = sorted(list(self.word))

        for word in word_list:
            word_letters = sorted(list(word))
            if word_letters == given_word_letters:
                matched_words.append(word)
        return matched_words
        