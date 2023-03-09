class Solution(object):#https://leetcode.com/problems/richest-customer-wealth/
    def maximumWealth(self, accounts):
        wealthiestAmt = 0
        for customer in accounts:
            x = sum(customer)
            if x > wealthiestAmt:
                wealthiestAmt = x
        return wealthiestAmt