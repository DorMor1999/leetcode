# Two Sum Problem

## Problem Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

**Assumptions:**
- Each input will have exactly one solution.
- You may not use the same element twice.
- The solution can be returned in any order.

## Examples
**Example 1**
- **Input:** `nums = [2,7,11,15]`, `target = 9`
- **Output:** `[0, 1]`
- **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

**Example 2**
- **Input:** `nums = [3,2,4]`, `target = 6`
- **Output:** `[1, 2]`
- **Explanation:** Because `nums[1] + nums[2] == 6`, we return `[1, 2]`.

**Example 3**
- **Input:** `nums = [3,3]`, `target = 6`
- **Output:** `[0, 1]`
- **Explanation:** Because `nums[0] + nums[1] == 6`, we return `[0, 1]`.

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Follow-up
Can you come up with an algorithm that has a time complexity of less than `O(n^2)`?


<hr>


# Two Sum Solution hash map Explanation

## Overview

This solution solves the Two Sum problem by utilizing a hash map (dictionary) to store the indices of the elements in the array. The algorithm efficiently finds the two indices whose corresponding numbers add up to the given target.

## Python Code Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a hash map (dictionary)
        hash_map = {}

        # Fill the hash_map with indices of each number
        for index in range(len(nums)):
            num = nums[index]
            if hash_map.get(f"{num}") is None:
                hash_map[f"{num}"] = []
            hash_map[f"{num}"].append(index)

        # Iterate through the nums list to find the two indices
        for index in range(len(nums)):
            num1 = nums[index]
            num2 = target - num1
            arr_test = hash_map.get(f"{num2}")
            if arr_test is not None:
                for num2index in arr_test:
                    if num2index != index:
                        return [index, num2index]

        # Return an empty list if no solution is found
        return []
```

## Detailed Explanation

### Step 1: Creating a Hash Map

The algorithm begins by creating an empty hash map (`hash_map`). This hash map is used to store each number from the `nums` array as a key, and the corresponding indices as values in a list. The purpose of this map is to allow for quick lookup of any number in the array.

- **Code:**
  ```python
  hash_map = {}
  ```

- **Filling the Hash Map:**
  The algorithm iterates through each number in the `nums` array, adding the index of each number to the hash map. If the number already exists as a key in the hash map, the index is appended to the list of indices.

  - **Example:** For `nums = [2, 7, 11, 15]`, the hash map after this step would look like:
    ```python
    {
        "2": [0],
        "7": [1],
        "11": [2],
        "15": [3]
    }
    ```

### Step 2: Finding the Pair of Indices

After constructing the hash map, the algorithm performs a second iteration through the `nums` array. For each number (`num1`), it calculates the complement (`num2`) required to reach the `target`. It then checks if this complement exists in the hash map.

- **Code:**
  ```python
  num2 = target - num1
  arr_test = hash_map.get(f"{num2}")
  ```

- **Check for Valid Pair:**
  If `num2` is found in the hash map, the algorithm further checks that the index of `num2` is not the same as the current index of `num1`. If this condition is satisfied, it returns the pair of indices.

  - **Example:** For `nums = [2, 7, 11, 15]` and `target = 9`, when the algorithm processes the number `2`, it finds that `7` is the complement, and the indices `[0, 1]` are returned.

### Step 3: Handling Edge Cases

If no valid pair of indices is found after iterating through the array, the algorithm returns an empty list.

- **Code:**
  ```python
  return []
  ```

## Time and Space Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the `nums` array. The algorithm makes two passes through the array: one to build the hash map and one to search for the pair of indices.

- **Space Complexity:** `O(n)`, as the hash map requires additional space to store the indices of the numbers.

## Conclusion

This solution is both time-efficient and space-efficient, making it a robust approach to solving the Two Sum problem, especially for large input sizes.


