class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = self.merge_sorted(nums1, nums2)
        merged_length = len(merged)
        if merged_length == 1:
            return float(merged[0])
        if merged_length % 2 == 0:
            return float(self.get_median_even(merged, merged_length))
        return float(self.get_median_uneven(merged, merged_length))
    
    def get_median_even(self, arr, arr_length):
        half_index_upper = int(arr_length / 2)
        half_index_lower = int(half_index_upper - 1)
        sum = arr[half_index_lower] + arr[half_index_upper]
        return sum / 2.0
    
    def get_median_uneven(self, arr, arr_length):
        half_index = int(arr_length / 2)
        return arr[half_index]
    
    def merge_sorted(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)

        p1 = 0
        p2 = 0

        merged = []
        while p1 < l1 or p2 < l2:
            if p1 == l1:
                merged.append(nums2[p2])
                p2 += 1
                continue

            if p2 == l2:
                merged.append(nums1[p1])
                p1 += 1
                continue

            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 +=1
                continue

            if nums2[p2] <= nums1[p1]:
                merged.append(nums2[p2])
                p2 += 1
        
        return merged