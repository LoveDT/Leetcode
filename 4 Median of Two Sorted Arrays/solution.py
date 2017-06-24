class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n / 2 + 1)
        else:
            return (self.findKth(nums1, nums2, n / 2) + self.findKth(nums1, nums2, n / 2 + 1)) / 2.0
        
    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        mid = min(len(nums1), k / 2)
        if nums1[mid - 1] < nums2[mid - 1]:
            return self.findKth(nums1[mid:], nums2, k - mid)
        else:
            return self.findKth(nums1, nums2[mid:], k - mid)