class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = list(pairs)
        states = []

        for i in range(len(arr)):
            j = i
            while j > 0 and arr[j - 1].key > arr[j].key:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
            states.append(list(arr))

        return states