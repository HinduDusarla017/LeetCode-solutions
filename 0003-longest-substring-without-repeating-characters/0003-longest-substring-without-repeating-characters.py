class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=set()
        j=0
        l=0
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[j])
                j+=1
            temp.add(s[i])
            l=max(l,i-j+1)
        return l

            