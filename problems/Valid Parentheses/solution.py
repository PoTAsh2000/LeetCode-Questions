class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openers_closers = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        openers_in_order = []

        for char in s:
            if self.isOpener(char):
                # add to openers in orders list and continue
                openers_in_order.append(char) 
                continue

            # char is a closer
            openers_in_order_len = len(openers_in_order)
            if openers_in_order_len == 0: 
                return False # this char is a closer while there are 0 openers found yet
        
            most_recent_opener = openers_in_order[openers_in_order_len - 1]
            expected_closer = openers_closers[most_recent_opener]
            if not expected_closer == char:
                return False # this closing character is not the closer that was expected for the most recent opener
            
            del openers_in_order[-1] # remove the most recent opener if the closer was valid

        
        if len(openers_in_order) > 0:
            return False # some openers were not closed

        return True
    
    def isOpener (self, char):
        openers = ["(", "{", "["]
        return char in openers