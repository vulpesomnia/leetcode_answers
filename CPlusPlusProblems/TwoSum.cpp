class Solution { //https://leetcode.com/problems/two-sum/ NOTE: I'm using the brute force method.
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();//Create the integer here so you dont have to call the function for the loops.
        for (int i = 0; i < n - 1; i++)//Last index isn't needed cause if it goes there theres no solution.
        {
            for (int v = i + 1; v < n; v++)
            {
                if (nums[i] + nums[v] == target)
                {
                    return {i, v};
                }
                    
            }
        }
        return {};//No solution found, returning an empty vector(array i think?).
    }
};