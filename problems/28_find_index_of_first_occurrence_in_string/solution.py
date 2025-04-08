class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for index, character in enumerate(haystack):
            if character != needle[0]: continue

            subString = haystack[index:]
            if subString.startswith(needle): return index

        return -1