class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # Count the occurrences of each element
        frequency_counter = {}
        for element in arr:
            frequency_counter[element] = frequency_counter.get(element, 0) + 1

        # Sort the list based on frequency using the .sort() method
        arr.sort(key=lambda x: (-frequency_counter[x], x))
        for i in range(k):
            arr.pop()
            
        return len(set(arr))