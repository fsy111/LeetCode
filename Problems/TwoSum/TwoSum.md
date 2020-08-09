# Two Sum

## Description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you may not use the same element twice.

### Example:
Given `nums = [2, 7, 11, 15]`, `target = 9`,

Because `nums[0] + nums[1] = 2 + 7 = 9`,
`return [0, 1]`.

## Solution
We use hash table to reduce the look up time from O(n) to O(1) by trading space for speed.

## Complexity Analysis:

Time complexity: O(n)
.
- We traverse the list containing n elements only once.
Each look up in the table costs only O(1) time.

- Space complexity : O(n).
The extra space required depends on the number of items stored in the hash table,
which stores at most n elements.

## Remark:
`Enumerate` is a built-in function of Python.
Its usefulness can not be summarized in a single line.
Yet most of the newcomers and even some advanced programmers are unaware of it.
It allows us to loop over something and have an automatic counter.
Here is an example:

``` python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
```

## Code:

``` python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i, num in enumerate(nums):
          n = target - num
          if n not in h:
            h[num] = i
          else:
            return [h[n], i]
```
