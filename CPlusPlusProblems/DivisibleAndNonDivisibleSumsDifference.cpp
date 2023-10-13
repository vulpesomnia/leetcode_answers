class Solution {//https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
public:
    int differenceOfSums(int n, int m) {
        int sum1 = 0;
        int sum2 = 0;
        for (int i = 1; i <= n; i++)
        {
            if (i % m != 0)//If remainder is 0
            {
                sum1 += i;
            }
            else
            {
                sum2 += i;
            }
        }
        return sum1 - sum2;//Return difference
    }
};