class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # could use hashmap to keep track of number and its frequency
        # once we kept track of every single i in nums, take the least frequent number
        # and place it at the beginning of array
        count = Counter(nums)
        def custom_sort(n):
            return (count[n], -n)
        nums.sort(key=custom_sort)
        # nums.sort(key=lambda n: (count[n], -n))
        return nums
