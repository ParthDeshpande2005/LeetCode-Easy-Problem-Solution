class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if(n%2==0 or n%3==0 or n%5==0):
        #     return True
        # else:
        #     return False
        if(n==0):
            return False
        else:
            while(n != 1):
                if(n%2==0):
                    n=n/2
                elif(n%3==0):
                    n=n/3
                elif(n%5==0):
                    n=n/5
                else:
                    return False
            return True