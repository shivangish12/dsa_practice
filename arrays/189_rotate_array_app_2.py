class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        reversed_nums = nums[::-1]
        reversed_f_half = reversed_nums[k-1::-1] 
        reversed_s_half = reversed_nums[n-1:k-1:-1] 
        nums[:] = reversed_f_half + reversed_s_half