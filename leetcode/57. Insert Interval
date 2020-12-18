def insert(self, intervals):
    res, merged = [], False
    for i, interval in enumerate(intervals):
        if interval[1] < newInterval[0] or merged:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            res.extend([newInterval, interval])
            merged = True
        else:
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
    if merged is False: res.append(newInterval)

    return res