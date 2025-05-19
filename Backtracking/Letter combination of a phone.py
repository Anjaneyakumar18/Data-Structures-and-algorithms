from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        l = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def backtrack(index, comb):
            if len(comb) == len(digits):
                result.append(''.join(comb))
                return
            for char in l[int(digits[index]) - 2]:
                comb.append(char)
                backtrack(index + 1, comb)
                comb.pop()
        result = []
        backtrack(0, [])
        return result
