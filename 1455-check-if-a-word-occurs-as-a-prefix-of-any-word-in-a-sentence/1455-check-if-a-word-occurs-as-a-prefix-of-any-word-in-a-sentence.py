class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sep_words = sentence.split()
        
        
        for i in range(len(sep_words)):
            count = 0
            for j in range(len(sep_words[i])):
                if(j < len(searchWord) and sep_words[i][j] == searchWord[j]):
                    count += 1
                    if count == len(searchWord):
                        return i + 1
        
        return -1
        