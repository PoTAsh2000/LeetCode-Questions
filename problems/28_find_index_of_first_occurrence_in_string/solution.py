class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        err = None
        while err == None:
            try:
                index = haystack.index(needle[0])
                substring = haystack[index:]
                if substring.startswith(needle):
                    return index
                haystack = haystack[:index] + "." + haystack[index + 1:]
            except ValueError as e:
                return -1