class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        result=0
        i=0
        j=0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                result+=1
                i+=1
            j+=1
        return result