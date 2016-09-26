import location
from trie import Trie

class Autocorrecter(object):
    """Autocorrects invalid words.

    Attributes:
        suggestion_limit: Maximum number of corrections to display.
        words: Set of valid words.
        trie: Prefix tree of valid words.
    """
    def __init__(self, dict_file):
        """Inits Autocorrecter with the words in dict_file."""
        self.suggestion_limit = 10
        self.words = self.makeDictionary(dict_file)
        self.trie = self.makeTrie(self.words)

    def makeDictionary(self, dict_file):
        """Creates a set of words from dict_file."""
        words = set()
        with open(dict_file, 'r') as f:
            for word in f:
                words.add(word.strip().lower())
        return words

    def makeTrie(self, words):
        """Creates a trie from dict_file."""
        trie = Trie()
        for word in words:
            trie.addWord(word)
        return trie

    def isWord(self, word):
        """Returns whether word is in the dictionary or not."""
        return word.lower() in self.words

    def removeLetter(self, word):
        """Returns the set of words formed by deleting a single letter."""
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
        """Returns the set of words formed by adding a single letter."""
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
        """Returns the set of words formed by swapping close letters."""
        words = set()
        for idx in range(len(word)):
            for c in location.getNeighbors(word[idx]):
                candidate = word[:idx] + c + word[idx + 1:]
                if candidate in self.words:
                    words.add(candidate)
        return words

    def printSet(self, words, n):
        """Prints n elements of a set."""
        count = 0
        for word in words:
            print(word + ' ', end='')
            count += 1
            if count == n:
                break

    def correct(self, word):
        """Corrects word."""
        word = word.lower()
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



