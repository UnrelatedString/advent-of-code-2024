#!/usr/bin/env python3

import numpy as np

def safe(report):
    diffs = report[:-1] - report[1:]
    if all(diffs < 0) or all(diffs > 0):
        return(all(abs(diffs) <= 3))

s = 0
for line in open(0):
    if not line.strip():
        continue
    report = np.array([*map(int, line.strip().split())])
    # wait the lines are so short I can just brute force this
    # diffs = report[:-1] - report[1:]
    # # # this catches 0 difference as well as mixed direction
    # # # big difference is never fixable! ...except at the ends never mind ugh
    # # flops = np.sign(diffs)[:-1] != np.sign(diffs)[1:]

    # sign = np.sign(sum(np.sign(diffs[:3])))
    # # 

    s += safe(report) or any(safe(np.concatenate((report[:i],report[i+1:]))) for i in range(*report.shape))



        

print(s)
