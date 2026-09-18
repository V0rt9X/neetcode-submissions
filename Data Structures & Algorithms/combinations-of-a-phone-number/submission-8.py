class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digToCh = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        
        res = []

        def backtrack(i, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            if i == len(digits):
                return
            
            for char in digToCh[digits[i]]:
                path.append(char)
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res if digits else []

        # T: O(b^d * w) - > O(dl^n * n) S: O(D) - > O(n)

        #dl == max(len(digit[i])) -> 4
        #digit[i] == letter in ith index to mapped digit
            