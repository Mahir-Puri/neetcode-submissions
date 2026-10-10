class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[x] stores the fewest coins needed to make amount x.
        # amount + 1 is larger than any possible valid answer, so it
        # works as a value meaning "currently unreachable".
        dp = [amount + 1] * (amount + 1)

        # Making amount zero requires no coins.
        dp[0] = 0

        # Build answers from smaller amounts to larger amounts.
        for current_amount in range(1, amount + 1):
            # Try every denomination as the last coin we add.
            for coin in coins:
                # We can only use this coin if it does not exceed the
                # current amount.
                if coin <= current_amount:
                    remaining_amount = current_amount - coin

                    # If the remaining amount is reachable, using this
                    # coin creates a valid candidate solution.
                    candidate = dp[remaining_amount] + 1

                    # Keep the solution that uses fewer coins.
                    dp[current_amount] = min(dp[current_amount], candidate)

        # If the target is still the sentinel value, no combination works.
        if dp[amount] == amount + 1:
            return -1

        # Otherwise, return the minimum number of coins found.
        return dp[amount]
