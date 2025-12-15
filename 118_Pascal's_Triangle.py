class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if(numRows==1):
            return [[1]]
        if(numRows==2):
            return [[1],[1,1]]
        else:
            c=[[1],[1,1],]
            for y in range (1,numRows-1):
                b=[1]
                for i in range(0,y):
                    b.append(c[y][i]+c[y][i+1])
                b.append(1)
                c.append(b)
            return c
        
        