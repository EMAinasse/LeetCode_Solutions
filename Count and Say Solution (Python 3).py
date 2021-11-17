#Python 3 Solution created in collaboration with Nizar Naitlho
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return Solution.say(self,Solution.countAndSay(self,n-1))
    
    def say(self,s):
        result = ""
        counter = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                counter += 1
            else:
                result += str(counter) + s[i]
                counter = 1
        result += str(counter) + s[-1]
        return result
