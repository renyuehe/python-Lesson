############ 自定义 排列组合
# 组合
def custom_combinations(iterable, r):
    pool = tuple(iterable)
    n = len(iterable)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

# 排列
def custom_permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(iterable)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


if __name__ == '__main__':
    ############### 自定义 排列组合 效率不如官方
    s = "123456"
    print(list(custom_combinations(s, 4)))
    s = "123456"
    print(list(custom_permutations(s, 3)))

    ############## 官方排列 组合
    from itertools import combinations
    from itertools import permutations

    # s = "123456"
    # print(list(combinations(s, 4)))
    # s = "123456"
    # print(list(permutations(s, 3)))
