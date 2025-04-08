class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        iter = 0
        longestBinaryNumber = max(len(a), len(b))
        
        aInt = 0
        bInt = 0
        while iter < longestBinaryNumber:
            if iter < len(a):
                aInt += int(a[iter]) * (2 ** (len(a) - 1 - iter))
            if iter < len(b):
                bInt += int(b[iter]) * (2 ** (len(b) - 1 - iter))
            iter += 1
        
        remainder = aInt + bInt
        if remainder == 0: return "0"

        result = ""
        while remainder != 0:
            bit = str(remainder % 2)
            result = bit + result
            remainder = remainder // 2
        return result
