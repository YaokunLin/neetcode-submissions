class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        letter_to_order = {letter : idx for idx, letter in enumerate(order)}

        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i + 1]

            if len(first_word) > len(second_word) and first_word[:len(second_word)] == second_word:
                # second_word is the prefix of first_word
                return False

            for j in range(len(first_word)):
                if letter_to_order[first_word[j]] > letter_to_order[second_word[j]]:
                    return False
                
                if letter_to_order[first_word[j]] < letter_to_order[second_word[j]]:
                    break
                
        return True
        
        