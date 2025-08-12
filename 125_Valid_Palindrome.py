class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        c=""
        for i in range(len(s)):
            if(s[i].isalnum()==True):
                c=c+s[i]
        if(c==c[::-1]):
            return True
        else:
            return False