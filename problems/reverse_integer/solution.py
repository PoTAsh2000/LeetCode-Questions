class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        reverse = x
        if x > 0:
            reverse = self.reverse_pos(x)
        else:
            reverse = self.reverse_neg(x)

        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0
        return reverse
    
    def reverse_pos(self, x):
        reverse = ""
        for char in reversed(str(x)):
            reverse += char
        return int(reverse)
    
    def reverse_neg(self, x):
        x = x * -1
        reverse = ""
        for char in reversed(str(x)):
            reverse += char
        reverse = int(reverse)
        reverse = reverse * -1
        return int(reverse)