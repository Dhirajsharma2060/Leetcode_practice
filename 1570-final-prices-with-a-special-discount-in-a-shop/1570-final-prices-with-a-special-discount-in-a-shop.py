class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        res = prices[:]  # Copy the original prices list

        for i in range(len(prices)):
            # Process the stack to apply discounts
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                res[index] -= prices[i]
            # Push current index to the stack
            stack.append(i)

        return res


# Taking user input
# if __name__ == "__main__":
    # prices = list(map(int, input("Enter prices separated by spaces: ").split()))
    # solution = Solution()
    # print("Final Prices after Discount:", solution.finalPrices(prices))
