class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        longest = 0

        chars_checked = {}
        for index in range(len(s)):
            char = s[index]
            
            
        return longest








        # longest_substring = 0
        # str_length = len(s)

        # for sub_str_start_i in range(str_length):
        #     chars_left = str_length - sub_str_start_i
        #     if chars_left <= longest_substring:
        #         print("substring '" + s[sub_str_start_i:str_length] + "' is less or equel then current longest[" + str(longest_substring) + "], no need to continue")
        #         return longest_substring

        #     processed = []
        #     for char_index in range(sub_str_start_i, str_length):
        #         char = s[char_index]

        #         if processed.__contains__(char):
        #             if len(processed) > longest_substring:
        #                 longest_substring = len(processed)
        #             break
        #         processed.append(char)

        #         if char_index == str_length - 1:
        #             print("end of string reached and no duplicates found - valid substring: " + s[sub_str_start_i:str_length])
        #             return len(processed)
        # return longest_substring

