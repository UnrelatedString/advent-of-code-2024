#!/usr/bin/env python3

rows = []
for line in open(0):
    if line.strip():
        rows.append([int(n) for n in line.strip().split()])

print(sum(abs(a-b) for a, b in zip(*map(sorted, zip(*rows)))))
