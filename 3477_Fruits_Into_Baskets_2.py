class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(fruits)):
            for y in range(len(baskets)):
                if(fruits[i]<=baskets[y]):
                    baskets.pop(y)
                    a=a+1
                    break
                
        return len(fruits)-a