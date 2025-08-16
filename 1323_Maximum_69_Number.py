class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
               
        a=str(num)
        a=a.replace("6","9",1)
        a=int(a)
        return a