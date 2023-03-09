class Solution(object):#https://leetcode.com/problems/fizz-buzz/
    def fizzBuzz(self, n):
        answer = []
        for i in range(n):
            answer.append(i+1)
        for num in range(len(answer)):
            x = answer[num]
            if x % 3 == 0:
                if x % 5 == 0:
                    answer[num] = "FizzBuzz"
                else:
                    answer[num] = "Fizz"
            elif x % 5 == 0:
                answer[num] = "Buzz"
            else:
                answer[num] = str(answer[num])
        return answer