#coding:utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        s = list(s)
        # 记录位置
        res_list = list()

        # 初始化 找到第一行的规律就好
        tmp_xp = 0
        turn = 1
        while tmp_xp < len(s):
            res_list.append(tmp_xp)
            tmp_xp = 2 * turn * (numRows - 1)
            turn += 1

        # 中间行
        init_len = len(res_list)
        for i in xrange(1, numRows - 1):
            for j in xrange(init_len):
                if res_list[j] - i > 0:
                    res_list.append(res_list[j] - i)
                if res_list[j] + i < len(s):
                    res_list.append(res_list[j] + i)
            # 边界
            if tmp_xp - i < len(s):
                res_list.append(tmp_xp - i)

        # 最后一行
        for j in xrange(init_len):
            if res_list[j] + numRows - 1 < len(s):
                res_list.append(res_list[j] + numRows - 1)

        return "".join(s[elem] for elem in res_list)

# 找规律就好
s = "AB"
numRows = 1
a = Solution()
print a.convert(s, numRows)