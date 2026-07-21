import re

class WordDictionary:
    def __init__(self):
        self.word_dict = [] 

    def addWord(self, word: str) -> None:
        self.word_dict.append(word)

    def search(self, word: str) -> bool:
      
        if "." not in word:
            if word in self.word_dict:
                return True
            else:
                return False
        else:
            for w in self.word_dict:
                if re.fullmatch(word, w):
                    return True
            return False

               

        
        



        
