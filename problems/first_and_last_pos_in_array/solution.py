class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums.__contains__(target):
            return [-1, -1]

        start = 0
        end = len(nums) - 1

        firstFound = False
        lastFound = False
        while not firstFound or not lastFound:
            if not firstFound:
                if nums[start] == target:
                    firstFound = True
                else:
                    start += 1
            
            if not lastFound:
                if nums[end] == target:
                    lastFound = True
                else:
                    end -= 1

        return [start, end]
