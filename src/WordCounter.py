class WordCounter:

    def __init__(self,sentence):
        self.sentence= sentence
        self.word_list=[]

    def count_words(self):
        self.word_list = self.sentence.split()
    def get_count_Words(self):
        return len(self.word_list)

    def get_shortest_word(self):
        shortest = min(self.word_list, key=len)
        return len(shortest)

    def get_longest_word(self):
        longest = max(self.word_list, key=len)
        return len(longest)






# sentence = "This is a test of the emergency broadcast system"
# word_counter = WordCounter(sentence)
# # word_counter.count_words()
# print(word_counter.get_word_count())    # Returns the number of all the words.
# # print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
# # print(word_counter.get_longest_word())  # Returns the length of the longest word.
