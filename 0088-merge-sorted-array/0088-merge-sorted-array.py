class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # res = []
        # nums1 = nums1[:m]
        # nums2 = nums2[:n]
        # i = 0
        # j = 0

        # while i < len(nums1) and j < len(nums2):
        #     res.append(nums1[i])
        #     res.append(nums2[j])  # ✅ fixed here
        #     i += 1
        #     j += 1

        # while i < len(nums1):
        #     res.append(nums1[i])
        #     i += 1
        # while j < len(nums2):
        #     res.append(nums2[j])
        #     j += 1
        # res.sort()    
        # nums1[:]=res
        nums1[:] = sorted(nums1[:m] + nums2[:n])
         
