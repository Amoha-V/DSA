class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 0
        dec = 0

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                inc += 1
            if nums[i] >= nums[i + 1]:
                dec += 1

        if inc == len(nums) - 1 or dec == len(nums) - 1:
            return True

        return False

   

        