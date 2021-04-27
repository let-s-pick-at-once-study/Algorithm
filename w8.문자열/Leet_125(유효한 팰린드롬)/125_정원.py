# Runtime: 48 ms, faster than 57.43% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15 MB, less than 38.39% of Python3 online submissions for Valid Palindrome.
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = re.findall("[a-z0-9]", s.lower())
        total_num = len(data)-1
        
        for i in range(total_num//2+1):
            if data[i] != data[total_num-i]:
                return False
        return True
