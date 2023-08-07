# leetcode 4. Median of Two Sorted Arrays
# solved : 20230806
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_combined = nums1 + nums2
        nums_combined.sort()
        median = -1
        n = len(nums_combined)
        for i in range(0,n):
            if n % 2 == 0:
                median = (nums_combined[n//2-1] + nums_combined[(n//2) ])/2
            elif n % 2 == 1:
                median = nums_combined[n//2]
        return median  


