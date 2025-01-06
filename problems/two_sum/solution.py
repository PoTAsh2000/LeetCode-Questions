class Solution(object):
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            diff_from_target = target - num
            if seen.__contains__(diff_from_target):
                return [seen[diff_from_target], i]
            seen[num] = i

        return None