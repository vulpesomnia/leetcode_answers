class Solution {//https://leetcode.com/problems/roman-to-integer
public:
    int romanToInt(string s) {
       std::unordered_map<char, int> romans = {
           {'M', 1000},
           {'D', 500},
           {'C', 100},
           {'L', 50},
           {'X', 10},
           {'V', 5},
           {'I', 1}
       }; 
       int size = s.size();
       int sum = 0;
       int prev_value = 0;
       for (int i = 0; i < size; i++)
       {
           int current_value = romans[s[i]];//Get current value from current character from current index of string using hash table.
           if(prev_value != 0)//If it isn't the start of the string or hasn't subtracted.
           {
               if (prev_value < current_value)//If current value is greater than previous then subtract cause roman numeral rules.
               {
                   sum += current_value - prev_value;
                   prev_value = 0;
               }
               else//Add to sum if no need for subtraction
               {
                   sum += prev_value;
                   prev_value = current_value;
               }
           }
           else
           {
               prev_value = current_value;
           }
       }
       return sum + prev_value;//Since at the end previous value isn't added to sum we add it here.
    }
};