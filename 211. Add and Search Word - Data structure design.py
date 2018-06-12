class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from string import ascii_lowercase
        self.dict = {}
        self.letters = ascii_lowercase

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dict[word] = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        idx = word.find('.')
        if idx == -1:
            if word in self.dict:
                return True
            return False
        for ch in self.letters:
            if self.search(word[:idx]+ch+word[idx+1:]):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)