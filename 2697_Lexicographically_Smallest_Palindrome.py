class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s="egcde"
        def big(a,b):
            if(a>b):
                return b
            else:
                return a

        for i in range((len(s)//2)+1):
            if(s[i]==s[len(s)-i-1]):
                pass
            else:
                z=big(s[i],s[len(s)-i-1])
                if(z==s[i]):
                    s=s[0:len(s)-i-1]+z+s[len(s)-i:]
                else:
                    s=s[0:i]+z+s[i+1:]

        return s