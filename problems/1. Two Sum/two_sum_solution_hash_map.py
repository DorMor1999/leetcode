from typing import List


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