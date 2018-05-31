#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

#For example,
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

#Given word1 = “coding”, word2 = “practice”, return 3.
#Given word1 = "makes", word2 = "coding", return 1.

#Note:
#You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = []
        w2 = []
        for i in range(len(words)):
          if words[i]==word1: w1.append[i]
             elif words[i]==word2: w2.append[i]
          #w1 = [i for i in xrange(len(words)) if words[i] == word1]
          #w2 = [i for i in xrange(len(words)) if words[i] == word2]
        return(min([abs(i-j) for i in w1 for j in w2])
