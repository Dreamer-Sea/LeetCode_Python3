from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or len(digits) > 4 or \
                digits == "0" or digits == "1" or digits == "*" or digits == "#":
            return []
        res = []
        phone_digits = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.backtracking(digits, "", phone_digits, res, 0)
        return res

    def backtracking(self, digits, temp: str, phone_digits, res: List[str], start: int):
        if len(temp) == len(digits):
            res.append(temp)
            return
        num_char = int(digits[start])
        num_alphabet_list = phone_digits[int(num_char)]
        for item in num_alphabet_list:
            self.backtracking(digits, temp + item, phone_digits, res, start + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))