# Runtime: 200 ms, faster than 38.03% of Python3 online submissions for Reverse String.
# Memory Usage: 18.5 MB, less than 73.45% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        total_num = len(s)-1
        for i in range(total_num//2+1):
            s[i], s[total_num-i] = s[total_num-i], s[i]
