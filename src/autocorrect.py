import location
from trie import Trie

class Autocorrecter(object):
    def __init__(self, dict_file):
        self.suggestion_limit = 10
        self.words = self.makeDictionary(dict_file)
        #  self.trie = self.makeTrie(self.words)

    def makeDictionary(self, dict_file):
        words = set()
        with open(dict_file, 'r') as f:
            for word in f:
                words.add(word.strip().lower())
        return words

    #  def makeTrie(self, words):
        #  trie = Trie()
        #  for word in words:
            #  trie.addWord(word)
        #  return trie

    def isWord(self, word):
        return word.lower() in self.words

    def getNeighborWords(self, word):
        word = word.lower()
        neighbor_words = set()
        for idx in range(len(word)):
            for c in location.getNeighbors(word[idx]):
                candidate = word[:idx] + c + word[idx + 1:]
                if candidate in self.words:
                    neighbor_words.add(candidate)
        return neighbor_words

    def printSet(self, words, n):
        count = 0
        for word in words:
            print(word + ' ', end='')
            count += 1
            if count == n:
                break

    def correct(self, word):
        if word in self.words:
            return

        neighbors = self.getNeighborWords(word)
        if len(neighbors) == 0 or self.suggestion_limit < 1:
            return

        count = 0
        print("Did you mean...")
        self.printSet(neighbors, self.suggestion_limit)
        print("?")



