class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        last_word = words[len(words) - 1]
        return len(last_word)
