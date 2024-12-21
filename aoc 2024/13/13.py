import re
import numpy as np

machines = open("input.txt").read().split('\n\n')
matches = [tuple(map(int, re.findall(r'(\d+)', machine))) for machine in machines]

def mincost(ax, ay, bx, by, px, py):
    a, arem = divmod(px*by - bx*py, ax*by - bx*ay)
    b, brem = divmod(ax*py - px*ay, ax*by - bx*ay)

    return 0 if arem or brem else a*3 + b

print(sum(mincost(*m) for m in matches))
base = 10000000000000
print(sum(mincost(ax, ay, bx, by, base + px, base + py)
          for ax, ay, bx, by, px, py in matches))
