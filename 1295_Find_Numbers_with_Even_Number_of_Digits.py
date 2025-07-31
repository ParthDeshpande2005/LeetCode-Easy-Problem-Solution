class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=0
        for i in nums:
            c=1
            while i/10>=1:
                i=i/10
                c=c+1
            if c%2==0:
                num=num+1
        return num