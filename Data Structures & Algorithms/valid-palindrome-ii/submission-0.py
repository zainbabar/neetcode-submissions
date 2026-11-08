class Solution:
    def validPalindromeHelper(self, s, l, r):
        left = l
        right = r
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        # same two pointer appraoch as valid palidrome 
        # however get one free mismatch
        # how to pick wehtehr we want to take the left or right side?
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            # not match, try out our deletion
            # try deleting the left char and seeing if its palidrome
            # if not try deleting the right char and seeing if its palindrome
            # just the first deletion is fine b/c this is a mismatch
            # we have to address. if it fails here no other deletion wowuld lhave worked
            else:
                remove_left = self.validPalindromeHelper(s, left+1, right)
                remove_right = self.validPalindromeHelper(s, left, right-1)
                return (remove_left or remove_right)
        return True


            
