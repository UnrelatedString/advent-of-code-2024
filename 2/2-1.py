#!/usr/bin/env python3

import numpy as np

s = 0
for line in open(0):
    if not line.strip():
        continue
    report = np.array([*map(int, line.strip().split())])
    diffs = report[:-1] - report[1:]
    if all(diffs < 0) or all(diffs > 0):
        s += all(abs(diffs) <= 3)

print(s)
