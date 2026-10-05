class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda interval: interval[1])

        selected = 1
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= last_end:
                selected += 1
                last_end = end

        return len(intervals) - selected