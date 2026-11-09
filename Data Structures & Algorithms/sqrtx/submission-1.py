class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest int whose square is <= x
        left = 1
        right = x 
        while left <= right:
            square_root = (left + right) // 2
            x_approx = square_root * square_root

            # our candidate is too small search larger ints
            if x_approx < x:
                left = square_root + 1
            # our candidate is too big, search smaller ints
            elif x_approx > x:
                right = square_root - 1
            else:
                return square_root
        
        # no exact int square root was found
        # right is the largest integer whos square is < x
        # left is the smallest int whose square is > x
        # actual sqrt lies betwene them so round down to the right
        return right


            