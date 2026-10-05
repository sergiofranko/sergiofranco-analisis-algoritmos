class Solution:
    def combinationSum(self, candidates, target):
        result = []
        current = []

        def search(start_index, remaining):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for index in range(start_index, len(candidates)):
                candidate = candidates[index]

                current.append(candidate)

                search(index, remaining - candidate)

                current.pop()

        search(0, target)

        return result