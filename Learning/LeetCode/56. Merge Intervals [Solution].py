"""
    Solution below is cleaner and more concise but similar approach
"""


def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        # If the current interval overlaps with the previous one, merge them
        if interval[0] <= merged[-1][1]:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        else:
            merged.append(interval)

    return merged

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1,6],[8,10],[15,18]]