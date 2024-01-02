#!/usr/bin/python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # For each element, iterate through the rest of the array
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current pair is equal to the target
                if nums[i] + nums[j] == target:
                    # If a pair is found, return the indices [i, j]
                    return [i, j]
