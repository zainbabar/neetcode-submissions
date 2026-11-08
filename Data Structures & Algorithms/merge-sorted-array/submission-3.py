class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        last = m + n - 1
        while (p1 >= 0 or p2 >= 0) and last >= 0:
            # both pointers are not exhausted yet
            if p1 > -1 and p2 > -1 and nums1[p1] >= nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1 
            elif p1 > -1 and p2 > -1:
                nums1[last] = nums2[p2]
                p2 -= 1 
            # one of the pointers is exhausted
            # if its the nums1 pointer then we still have more 
            # from nums2 to move over
            elif p2 > -1:
                nums1[last] = nums2[p2]
                p2 -= 1 
            # if nums2 is exhausted, the rest is already is nums1
            # so we can just break out
            else:
                break


            last -= 1 


