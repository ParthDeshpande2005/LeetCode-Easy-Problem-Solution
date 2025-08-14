class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
    
        c=[]
        for i in range(1,len(num)-1):
            if(num[i]==num[i+1]==num[i-1]):
                c.append(3*num[i])
        
        if(c==[]):
            return ""
        else:
            c.sort(reverse=True)
            return c[0]