class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        for i in xrange(0, len(x) / 2):
            if x[i] != x[len(x)-1-i]:
                return False
        return True

x = -1
a = Solution()
print a.isPalindrome(x)