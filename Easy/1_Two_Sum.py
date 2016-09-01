class Solution(object):
    def twoSum(self, nums, target):
        dic = dict()
        """
        dic 记录nums里A对应的B的信息
            key: B
            value: nums里A值的位置
        注:(A表示nums里的元素  B表示target-A)
        """
        for i in xrange(len(nums)):
            if nums[i] not in dic: #没有匹配
                dic[target - nums[i]] = i #记录B的信息
            else: #找到匹配
                return [i, dic[nums[i]]]

"""
代码来自https://discuss.leetcode.com/topic/53542/python-o-n-solution-nice-idea
思路很好，比自己写的强多了
"""
