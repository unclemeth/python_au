def eraseOverlapIntervals(self, intervals):
    start, cnt = float('+inf'), 0
    for s, e in sorted(intervals, key=lambda x: x[0], reverse=True):
        if e <= start:
            start = s
        else:
            cnt += 1
    return cnt