class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dic = dict() #用来记录字符串里每个字符的最新位置(从前往后遍历字符串)
        return_int = count_pos = now_value = 0
        """return_int 表示字符串中最长无重复子串的长度
           count_pos  表示字符 在字符串的位置
           now_value  表示当前位置的无重复子串的长度，并不是当前位置最大无重复子串长度
                      (如果出现相同的字符 now_value的值会对应变化的)
        """
        for elem in s:
            count_pos += 1
            if elem not in char_dic: 
                char_dic[elem] = count_pos
                now_value += 1
            else: #出现相同的字符
                if count_pos - char_dic[elem] > now_value: now_value += 1 #上个字符出现的比较远，那么当前位置的长度+1
                else: now_value = count_pos - char_dic[elem] #上个子字符出现的比较近，那么当前位置的长度为 本次的字符位置减上回字符的位置
            if return_int < now_value: return_int = now_value
            char_dic[elem] = count_pos
        return return_int

a = Solution()
print a.lengthOfLongestSubstring("aaabcabcdd")

"""
自己的思路写的
没有参照讨论区给的意见
有进步
"""
