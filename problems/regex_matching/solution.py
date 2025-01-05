import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        result = re.match(p, s)
        return result != None and result.group(0) == s