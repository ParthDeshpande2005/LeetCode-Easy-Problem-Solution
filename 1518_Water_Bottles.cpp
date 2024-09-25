class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) 
    {

        int o=numBottles;
        int a=o;
        while(o>=numExchange)
        {
            int x=o/numExchange;
            a=a+x;
            int num1=o%numExchange;
            o=o/numExchange;
            o=o+num1;    
        }
        return a;
    }
};