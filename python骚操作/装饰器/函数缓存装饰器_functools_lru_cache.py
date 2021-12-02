import time
def fibonacci(n):
    """斐波那契函数"""
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
    stime = time.time()
    print(fibonacci(34))  # 没有使用缓存，则需要几秒钟的时间
    print("total time is %.3fs" % (time.time() - stime))


'''
functools.lru_cache是一个函数缓存装饰器，lru说明了算法，
Least Recently Used，这个算法被用在很多地方，比如OS做虚拟内存置换的时候。

LRU算法的思想：将最近最少使用到的区域，进行某个动作，比如置换到硬盘，或者从缓存中删除。

functools.lru_cache装饰函数后，会将函数的输入和输出进行缓存，
如果再下次调用此函数时，出现了相同的输入，那么相同的输出就可直接从缓存中提取，
函数体本身无需再次执行，用一点内存，加快了速度。


lru_cache(maxsize=128, typed=False)
    Least-recently-used cache decorator.

    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.

    If *typed* is True, arguments of different types will be cached separately.
    For example, f(3.0) and f(3) will be treated as distinct calls with
    distinct results.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().
    Access the underlying function with f.__wrapped__.

    See:  http://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
'''

import functools
@functools.lru_cache(maxsize=300)
def fibonacci(n):
    """斐波那契函数"""
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
    stime = time.time()
    ret = fibonacci(34)
    print(ret)
    print("total time is %.3fs" % (time.time() - stime))


'''
如果使用了lru_cache，计算用时被大大减少，测试计算时间为0s。
这是因为我们在使用fibonacci递归函数时，会重复计算值。
使用了lru_cache后，所有的重复计算只会执行一次。
'''