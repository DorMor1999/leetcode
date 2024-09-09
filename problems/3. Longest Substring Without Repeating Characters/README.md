# 3. Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

### Examples

#### Example 1:
- **Input**: `s = "abcabcbb"`
- **Output**: `3`
- **Explanation**: The answer is `"abc"`, with the length of 3.

#### Example 2:
- **Input**: `s = "bbbbb"`
- **Output**: `1`
- **Explanation**: The answer is `"b"`, with the length of 1.

#### Example 3:
- **Input**: `s = "pwwkew"`
- **Output**: `3`
- **Explanation**: The answer is `"wke"`, with the length of 3.
  - Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

### Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.


<hr>


## Solution Explanation

The provided code solves the problem of finding the length of the longest substring without repeating characters using a sliding window approach and an ASCII-based boolean array. Here's a step-by-step explanation:

### Code Implementation

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize 'result' to track the length of the longest substring found
        result = 0
        # Initialize 'i' to serve as the starting index of the current substring
        i = 0
        
        # Continue the loop while the remaining length of the string can potentially give a longer substring
        while len(s) - i > result:
            # Create a boolean array of size 128 to track the presence of ASCII characters
            ascii_list = [False] * 128
            # Initialize 'counter' to count the length of the current substring without repeating characters
            counter = 0
            
            # Iterate over the substring starting from index 'i'
            for j in range(i, len(s)):
                # Get the ASCII value of the current character
                ascii_value = ord(s[j])
                
                # If the character has been seen before in the current substring, exit the loop
                if ascii_list[ascii_value]:
                    break
                else:
                    # Mark the character as seen in the boolean array
                    ascii_list[ascii_value] = True
                    # Increment the counter as this character extends the current substring
                    counter += 1
                    # Update 'result' if the current substring length is greater than the previous maximum
                    if result < counter:
                        result = counter
            # Move the starting index 'i' to the next position for the next iteration
            i += 1

        # Return the length of the longest substring without repeating characters
        return result
```

### Complexity Analysis

- **Time Complexity**: O(n^2)
  - The algorithm involves a nested loop where `i` ranges from 0 to `n` and the inner loop runs from `i` to `n`. In the worst case, this results in O(n^2) time complexity.

- **Space Complexity**: O(1)
  - The space complexity is O(1) because the size of the `ascii_list` is constant (128 elements), regardless of the input size. 
