class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # remove leading && trailing white space, if result is None or empty return 0
        s = s.strip()
        if s == None or len(s) == 0:
            return 0
        
        # check if num is positive or negative and remove identifier (index 0) from string if no identifier was found, the value is always positive
        is_negative = False
        if s[0] == "-":
            is_negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        # remove leading zeros
        s = s.lstrip("0")

        # validate each char in string. if its not a digit break the loop, otherwise append to the result
        result = ""
        for char in s:
            if not(str(char).isdigit()):
                break
            result += str(char)

        if result == None or result == "" or result == "0":
            return 0

        # if the input was negative, if so, convert current always positive result to negative number
        result = int(result)
        if is_negative:
            result = result * -1

        # check if in range of 32 bit int length, if not, round to upper or lower length of 32 bit int
        if result < -2**31:
            result = -2**31
        if result > 2**31 - 1:
            result = 2**31 - 1

        return result