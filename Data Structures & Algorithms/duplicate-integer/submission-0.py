class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # If lengths differ, duplicates were removed by the set
        return len(nums) != len(set(nums))