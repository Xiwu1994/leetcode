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
脑子里的思路是，想用时间复杂度为O(n)来解决问题+空间换时间的思路
然后琢磨着需要保存什么样的数据，用什么样的数据结构
"""

"""
以下是讨论区的代码,大体思路一样,保存的数据不一样
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0  #返回值
        tmpstr = "" #当前最长的子串(并不是全局最长，且没有重复字符)
        for ch in s:
            if not ch in tmpstr:
                tmpstr = tmpstr + ch
                if len(tmpstr) > max:
                    max = len(tmpstr)
            else:
                tmpstr = tmpstr[tmpstr.find(ch)+1:] + ch
            print "tmpstr: {0}".format(tmpstr)
        return max
