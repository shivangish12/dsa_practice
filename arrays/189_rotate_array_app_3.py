class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        count=0
        nums_1=[0]*(len(nums))
        for idx in range(len(nums)):
            if idx+k < len(nums):
                nums_1[idx+k]=nums[idx]
            elif count<k:
                nums_1[count]=nums[idx]
                count+=1
        for i in range(n):
            nums[i] = nums_1[i]