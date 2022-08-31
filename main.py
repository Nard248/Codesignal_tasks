a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]


def solution(a, b):
    if len(a) != len(b):
        return False
    miss_count = 0
    miss_value = 0
    a_miss_index = 0
    b_miss_index = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            miss_value = a[i]
            miss_count += 1
            a_miss_index = i
        if miss_count >= 3:
            return False
        if b[i] == miss_value:
            b_miss_index = i
    if a[a_miss_index] == b[b_miss_index]:
        return True
    else:
        return False

def solution(grid):
    rows = grid
    cols = zip(*grid)
    subs = []

    for i in range(0,7,3):
        for j in range(0,7,3):
            subs.append([grid[r][c] for r in range(i,i+3) for c in range(j,j+3)])

    def isvalid(arr):
        nums = [x for x in arr if str.isdigit(x)]
        return len(nums) == len(set(nums))

    return all([
        all(map(isvalid, rows)),
        all(map(isvalid, cols)),
        all(map(isvalid, subs))
    ])