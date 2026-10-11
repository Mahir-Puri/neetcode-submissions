
class Solution:
    def rob(self, nums: list[int]) -> int:
        two_houses_back = 0
        one_house_back = 0

        for money in nums:
            rob_current = two_houses_back + money
            skip_current = one_house_back

            current_best = max(rob_current, skip_current)

            two_houses_back = one_house_back
            one_house_back = current_best

        return one_house_back
