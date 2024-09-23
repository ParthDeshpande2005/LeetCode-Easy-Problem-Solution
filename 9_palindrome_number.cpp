class Solution {
public:
    bool isPalindrome(long long x)
    {
        if(x<0)
        {
            return false;
        }
        long long reverse=0;
        long long temp=x;

            while(x!=0)
            {    
                long long a=x%10;
                reverse=reverse*10+a;
                x /= 10;
            }
        return (reverse==temp);    
    }    
};