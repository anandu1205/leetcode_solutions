class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        # Maximum normal subarray
        currMax = maxSum = nums[0]

        # Minimum normal subarray
        currMin = minSum = nums[0]

        for i in range(1, len(nums)):

            currMax = max(nums[i], currMax + nums[i])
            maxSum = max(maxSum, currMax)

            currMin = min(nums[i], currMin + nums[i])
            minSum = min(minSum, currMin)

        # If all numbers are negative
        if maxSum < 0:
            return maxSum

        # Circular sum = total - minimum subarray
        circularSum = total - minSum

        return max(maxSum, circularSum)
    

        