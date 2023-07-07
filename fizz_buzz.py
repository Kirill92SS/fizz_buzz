from typing import List


class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        out_lst: List[str] = []
        for _ in range(1, n + 1):
            if not (_ % 3) and not(_ % 5):
                out_lst.append("FizzBuzz")
            elif not (_ % 3):
                out_lst.append("Fizz")
            elif not (_ % 5):
                out_lst.append("Buzz")
            else:
                out_lst.append(str(_))
        return out_lst


print(Solution().fizzBuzz(15))
