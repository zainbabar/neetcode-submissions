class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # go thru the string, if char is alphanumeric join it to the new result string
        s = ''.join(char for char in s if char.isalnum())
        # so now we have lowercased and only alnum string 
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True



