class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stringArr = ''.join(map(str, digits))
        plusOne = str(int(stringArr) + 1)
        return list(map(int, plusOne))