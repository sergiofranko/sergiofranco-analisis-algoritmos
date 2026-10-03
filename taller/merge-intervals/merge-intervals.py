class Solution:
    def merge(self, intervals):
        ordered = self.merge_sort(intervals)
        result = []

        for start, end in ordered:
            if not result or start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result

    def merge_sort(self, intervals):
        if len(intervals) <= 1:
            return intervals

        middle = len(intervals) // 2

        first_half = self.merge_sort(intervals[:middle])
        second_half = self.merge_sort(intervals[middle:])

        return self.combine(first_half, second_half)

    def combine(self, first_half, second_half):
        ordered = []
        first_index = 0
        second_index = 0

        while (first_index < len(first_half) and
               second_index < len(second_half)):

            if first_half[first_index][0] <= second_half[second_index][0]:
                ordered.append(first_half[first_index])
                first_index += 1
            else:
                ordered.append(second_half[second_index])
                second_index += 1

        ordered.extend(first_half[first_index:])
        ordered.extend(second_half[second_index:])

        return ordered
