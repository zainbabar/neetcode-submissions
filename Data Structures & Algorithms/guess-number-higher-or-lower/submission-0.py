# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            num = (left + right) // 2
            if guess(num) == -1: # guess is higher
                # right endpoint is 1 lower than our guess
                # can rule out anything our guess and bigger now
                right = num - 1
            elif guess(num) == 1: # guess is lower
                # left enpoint 1 bigger than our guess
                # rule out anything == to our guess and smaller now
                left = num + 1
            else:
                return num