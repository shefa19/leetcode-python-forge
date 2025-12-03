'''Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.

Return the chosen digit as an integer.

The frequency of a digit x is the number of times it appears in the decimal representation of n.
 

Example 1:

Input: n = 1553322

Output: 1

Explanation:

The least frequent digit in n is 1, which appears only once. All other digits appear twice.

Example 2:

Input: n = 723344511

Output: 2

Explanation:

The least frequent digits in n are 7, 2, and 5; each appears only once.

 

Constraints:

1 <= n <= 231​​​​​​​ - 1'''

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        cnt = Counter(n)

        s = set(n)
        min_val = float('inf')
        x = None
        for i in sorted(s):
            if cnt[i] < min_val:
                x = int(i)
                min_val = cnt[i]

        return x