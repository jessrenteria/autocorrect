import location
from trie import Trie

class Autocorrecter(object):
    def __init__(self, dict_file):
        self.suggestion_limit = 10
        self.words = self.makeDictionary(dict_file)
        self.trie = self.makeTrie(self.words)

    def makeDictionary(self, dict_file):
        words = set()
        with open(dict_file, 'r') as f:
            for word in f:
                words.add(word.strip().lower())
        return words

    def makeTrie(self, words):
        trie = Trie()
        for word in words:
            trie.addWord(word)
        return trie

    def isWord(self, word):
        return word.lower() in self.words

    def removeLetter(self, word):
        words = set()
        if len(word) < 2:
            return words

        if word[1:] in self.words:
            words.add(word[1:])

        node = self.trie.getNode(word[0])
        for idx in range(1, len(word)):
            candidate = word[:idx] + word[idx + 1:]
            if candidate in self.words:
                words.add(candidate)
        return words

    def addLetter(self, word):
        words = set()
        node = self.trie
        for idx in range(0, len(word) + 1):
            for c in node.edges:
                candidate = word[:idx] + c + word[idx:]
                if candidate in self.words:
                    words.add(candidate)
            if idx < len(word):
                node = node.getNode(word[idx])
            if node == None:
                break
        return words

    def getNeighbors(self, word):
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

        corrections = (self.removeLetter(word)
                       | self.addLetter(word)
                       | self.getNeighbors(word))
        if len(corrections) == 0 or self.suggestion_limit < 1:
            print("Not a valid word!")
            return

        count = 0
        print("Did you mean...")
        self.printSet(corrections, self.suggestion_limit)
        print("?")



