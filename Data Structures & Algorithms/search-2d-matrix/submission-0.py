class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first rule out sub lists? 
        outer_left = 0
        outer_right = len(matrix) - 1
        while outer_left <= outer_right:
            mid = (outer_left + outer_right) // 2
            cur_list = matrix[mid]
            # target is somewhere within this list, pick this list to search
            if cur_list[0] <= target and cur_list[-1] >= target:
                inner_left = 0
                inner_right = len(cur_list) - 1
                while inner_left <= inner_right:
                    inner_mid = (inner_left + inner_right) // 2
                    if cur_list[inner_mid] < target:
                        inner_left = inner_mid + 1
                    elif cur_list[inner_mid] > target:
                        inner_right = inner_mid - 1
                    else:
                        return True
                return False
            # target is not within the range of this list
            # either it is smaller than the beginning (on the left side)
            # or bigger than the ending (on the right side)
            elif cur_list[0] > target: # smallest val in cur list is bigger than targ 
                outer_right = mid - 1
            elif cur_list[-1] < target: # largest val in cur list is smaller than targ
                outer_left = mid + 1
        return False
