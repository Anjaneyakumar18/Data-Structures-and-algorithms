class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        low, right = 0, num // 2
        while low <= right:
            mid = (low + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                right = mid - 1
        return False
