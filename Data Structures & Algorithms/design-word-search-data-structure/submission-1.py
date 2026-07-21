import re

class WordDictionary:
    def __init__(self):
        self.word_dict = [] 

    def addWord(self, word: str) -> None:
        self.word_dict.append(word)

    def search(self, word: str) -> bool:
        for w in self.word_dict:
            if len(w) != len(word):
                continue
            matched = True
            for i in range(len(word)):
                if word[i] != "." and word[i] != w[i]:
                    matched = False
                    break
            if matched == True:
                return True
        return False
      
       

               

        
        



        
