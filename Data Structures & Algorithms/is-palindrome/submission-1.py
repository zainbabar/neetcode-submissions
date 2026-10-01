class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0
        j = l - 1 # index to the end
        # while we are not at the same index
        # if we are same index, pointers touch, so break out 
        while(i < j): # skip any no
            if s[i].isalnum() == False:
                i += 1
                continue
            if s[j].isalnum() == False:
                j -= 1
                continue

            # both chars are alnum
            # check if they match, both ends are the same
            if s[i].lower() != s[j].lower(): # dont match break out
                return False
            else:  # do match, continue next 2
                i += 1
                j -= 1
            
        return True
            




            