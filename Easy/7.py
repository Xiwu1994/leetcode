class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = list(str(x))
        x.reverse()
        if x[-1] == "-":
            x = [x[-1]] + x[:-1]
        x = int("".join(x))
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x