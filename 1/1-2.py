#!/usr/bin/env python3

from collections import Counter

rows = []
for line in open(0):
    if line.strip():
        rows.append([int(n) for n in line.strip().split()])

l, r = zip(*rows)
m = Counter(r) # this actually works in either direction and I could dot product the histograms but I don't think it actually saves any time or whateve

print(sum(a * m[a] for a in l))
