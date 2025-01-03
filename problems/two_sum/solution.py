class Solution(object):
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        for iter1 in range(len(nums)):
            for iter2 in range(len(nums)):
                if iter1 == iter2:
                    continue
                
                sum = nums[iter1] + nums[iter2]
                if sum == target:
                    return self.getResult(iter1, iter2)
        return None
        
    def getResult(self, i1, i2):
        result = []
        result.append(i1)
        result.append(i2)
        return result