# Time : 4ms (98.98%) Space : 11.93 MB (7.82%)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=''
        big_word=word1 if len(word1)>=len(word2) else word2
        small_word=word2 if big_word==word1 else word1 
        print(big_word, small_word)

        for i in range(len(small_word)):
            merged+=(word1[i]+word2[i])

        merged+=big_word[len(small_word):]

        return merged
        