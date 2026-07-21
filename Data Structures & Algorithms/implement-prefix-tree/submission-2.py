class node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = node()

    def insert(self, word: str) -> None:
        curr = self.root
        for chr in word:
            if chr not in curr.children:
                curr.children[chr] = node()
            curr = curr.children[chr]
        curr.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for chr in word:
            if chr not in curr.children:
                return False
            curr = curr.children[chr]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for chr in prefix:
            if chr not in curr.children:
                return False
            curr = curr.children[chr]
        return True
        
        