class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = list()
        str = list(str)
        first_flag = 1
        for elem in str:
            if first_flag:
                if elem == " ":
                    continue
                else:
                    first_flag = 0
            if elem not in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
            if elem in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                res.append(elem)
        try:
            res = int("".join(res))
        except:
            return 0
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        else:
            return res

# 我真是服了..