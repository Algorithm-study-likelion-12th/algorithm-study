from bisect import bisect_left


def is_included(c, w, n):
    if c in w:
        return 1
    i = 0
    j = n - 1
    while i < j:
        sum = w[i] + w[j]
        if sum == c:
            return 1
        elif sum > c:
            j -= 1
        else:
            diff = c - sum
            res = bisect_left(w, diff)
            if res < n and w[res] == diff and res != i and res != j:
                return 1
            i += 1
    return 0


n, c = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
print(is_included(c, w, n))
