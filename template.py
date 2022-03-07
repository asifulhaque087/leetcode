from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


class Solution:
    def twoSum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))

# https://nextjs-tailwind-hulu-clone.vercel.app/
# https://nextjs-tailwind-google-clone.vercel.app/
# https://reactjs-video-chat-one.netlify.app/
