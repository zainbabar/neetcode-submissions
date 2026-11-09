class Solution:
    def mySqrt(self, x: int) -> int:
        # what number multiplied by itself is x? 
        left = 1
        right = x 
        while left <= right:
            square_root = (left + right) // 2
            x_approx = square_root * square_root

            # our approx is too small, i.e. our square root is too small
            if x_approx < x:
                left = square_root + 1
            # our approx is too big, i.e. our square root is too big
            elif x_approx > x:
                right = square_root - 1
            else:
                return square_root
        
        # either we perfectly get the square root as an integer
        # or we didnt get exact and we have to get the rounded down one 
        # if we didnt. get a perfect and right = left - 1
        # we know that the square root sits somewhere between (right, left)
        # pick right b/c that is the rounded down
        return right


            