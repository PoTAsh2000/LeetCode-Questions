class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = int(self.binaryToInt(a)) + int(self.binaryToInt(b))

        if sum == 0:
            return "0"
        
        return self.intToBinary(sum)
            
    def intToBinary(self, remainder):
        result = ""
        while remainder != 0:
            bit = str(remainder % 2)
            result = bit + result
            remainder = remainder // 2
        return result

    def binaryToInt(self, binaryNumber):
        result = 0
        power = len(str(binaryNumber)) - 1
        for i in binaryNumber:
            result += int(i) * (2 ** power)
            power -= 1
        return result
        