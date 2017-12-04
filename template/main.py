#!/usr/bin/env python3

import bisect
import fileinput
import hashlib
import heapq
import itertools
import json
import re
from collections import defaultdict, deque, namedtuple

lines = [l.strip().split() for l in open('input').readlines() if l.strip()]
try:
    nums = [[int(x) for x in l] for l in lines]
    lines = nums
except:
    pass

for line in lines:
    print(line)
