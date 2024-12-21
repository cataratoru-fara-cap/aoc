from numpy import array as A, unique as uniq
from scipy.ndimage import label
from scipy.signal import convolve2d

G = A([list(line.strip()) for line in open("demo.txt")])
S = lambda A: abs(A).sum()

ans = A([0,0])

