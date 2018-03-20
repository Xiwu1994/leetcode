#coding:utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            return self.process(nums1, nums2)
        else:
            return self.process(nums2, nums1)

    def process(self, nums1, nums2):
        """
        len(nums1) <= len(num2)
        """
        # 处理边界条件
        if len(nums1) == 0:
            return self.findMedianValue(nums2)
        mid_nums1 = self.findMedianValue(nums1)
        mid_nums2 = self.findMedianValue(nums2)
        if len(nums1) == 1:
            if len(nums2) == 1:
                return (mid_nums1 + mid_nums2) / 2.0
            # A: [3]
            # B: [1,2,3,4,5]
            elif len(nums2) % 2:
                if mid_nums1 <= nums2[(len(nums2) - 1) / 2 - 1]:
                    return (nums2[(len(nums2) - 1) / 2 - 1] + mid_nums2) / 2.0
                elif nums2[(len(nums2) - 1) / 2 + 1] > mid_nums1 > nums2[(len(nums2) - 1) / 2 - 1]:
                    return (mid_nums1 + mid_nums2) / 2.0
                else:
                    return (nums2[(len(nums2) - 1) / 2 + 1] + mid_nums2) / 2.0
            # A: [3]
            # B: [2,3,4,5]
            else:
                if nums2[(len(nums2) + 1) / 2] <= nums1[0]:
                    return nums2[(len(nums2) + 1) / 2]
                elif nums2[(len(nums2) - 1) / 2] >= nums1[0]:
                    return nums2[(len(nums2) - 1) / 2]
                else:
                    return nums1[0]
        # A:    [3, 4, 5, 6]
        # B: [1, 1, 2, 8, 9, 9]
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            if nums1[len(nums1)/2-1]>=nums2[len(nums2)/2-1] and nums1[len(nums1)/2]<=nums2[len(nums2)/2]:
                return (nums1[len(nums1) / 2 - 1] + nums1[len(nums1) / 2]) / 2.0
            elif nums2[len(nums2)/2-1]>=nums1[len(nums1)/2-1] and nums2[len(nums2)/2]<=nums1[len(nums1)/2]:
                return (nums2[len(nums2) / 2 - 1] + nums2[len(nums2) / 2]) / 2.0

        if mid_nums1 == mid_nums2:
            return mid_nums1
        # 两个数组都切  nums1的一半 (切的长度要一样)
        elif mid_nums1 < mid_nums2:
            nums2 = nums2[:len(nums2) - (len(nums1) - len(nums1) % 2) / 2]
            nums1 = nums1[(len(nums1) - len(nums1) % 2) / 2:]
        else:
            nums2 = nums2[len(nums1) - (len(nums1) + len(nums1) % 2) / 2:]
            nums1 = nums1[:(len(nums1) + len(nums1) % 2) / 2]
        return self.process(nums1, nums2)

    def findMedianValue(self, array):
        if len(array) % 2:
            return array[(len(array)-1)/2]
        else:
            return (array[len(array)/2] + array[len(array)/2-1])/2.0
