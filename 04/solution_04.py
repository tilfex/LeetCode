class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2
        
        nums1.sort()
        if len(nums1)%2 == 0:
            n1=nums1[int((len(nums1)/2))-1]
            n2=nums1[int((len(nums1)/2))]
            return ((n1+n2)/2)
        else:
            return nums1[(int((len(nums1))/2))]