class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        cnt=0
        while i < len(s):
            if s[i] == "I":
                if i+1 < len(s) and s[i+1] == "V":
                    cnt += 4
                    i += 2
                elif i+1 < len(s) and s[i+1] == "X":
                    cnt += 9
                    i += 2
                else:
                    cnt += 1
                    i += 1
            elif s[i] == "V":
                cnt += 5
                i += 1
            elif s[i] == "X":
                if i+1 < len(s) and s[i+1] == "L":
                    cnt += 40
                    i += 2
                elif i+1 < len(s) and s[i+1] == "C":
                    cnt += 90
                    i += 2
                else:
                    cnt += 10
                    i += 1
            elif s[i] == "L":
                cnt += 50
                i += 1
            elif s[i] == "C":
                if i+1 < len(s) and s[i+1] == "D":
                    cnt += 400
                    i += 2
                elif i+1 < len(s) and s[i+1] == "M":
                    cnt += 900
                    i += 2
                else:
                    cnt += 100
                    i += 1
            elif s[i] == "D":
                cnt += 500
                i += 1
            elif s[i] == "M":
                cnt += 1000
                i += 1
        return cnt