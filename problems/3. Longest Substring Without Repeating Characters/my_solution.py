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