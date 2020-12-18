from random import randint, seed, shuffle
from typing import List


def brute_force(nums: List[int]):
    ln = len(nums)
    max_total = 0
    all_seqs = set()
    for i in range(10000000):
        seq = []
        nums2 = nums.copy()
        total = 0
        for j in range(ln):
            k = randint(0, ln-1-j)
            total += nums2[k] * (nums2[k-1] if k > 0 else 1) * (nums2[k+1] if k < ln-1-j else 1)
            seq.append(nums2[k])
            nums2.pop(k)

        if total >= max_total:
            max_total = total
            print(f'{i} - {max_total} - {seq}')
            all_seqs.add(tuple(seq))

        # if i % 10000 == 0:
        #     print(f'{i} - {max_total}')

    print(max_total)
    print('\n'.join(str(i) for i in all_seqs))


# brute_force([9, 76, 64, 21])

seed(0)
_a = list(set([randint(1, 20) for i in range(10)]))
shuffle(_a)
print(_a)
brute_force(_a)
