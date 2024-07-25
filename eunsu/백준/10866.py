from collections import deque
import sys


class Deque:

    def main(self):
        n = int(input())
        box = deque()
        for i in range(n):
            inputs = input().split()
            order = inputs[0]
            num = int(inputs[1]) if len(inputs) > 1 else None
            if num is not None:
                num = int(num)
            method = getattr(self, order, None)
            if method:
                box, result = method(box=box, num=num)
                if result is not None:
                    print(result)

    def push_front(self, box, num=None):
        box.appendleft(num)
        return box, None

    def push_back(self, box, num=None):
        box.append(num)
        return box, None

    def pop_front(self, box, num=None):
        if len(box) == 0:
            result = -1
        else:
            result = box.popleft()
        return box, result

    def pop_back(self, box, num=None):
        if len(box) == 0:
            result = -1
        else:
            result = box.pop()
        return box, result

    def size(self, box, num=None):
        return box, len(box)

    def empty(self, box, num=None):
        return box, int(not box)

    def front(self, box, num=None):
        if len(box) == 0:
            result = -1
        else:
            result = box[0]
        return box, result

    def back(self, box, num=None):
        if len(box) == 0:
            result = -1
        else:
            result = box[-1]
        return box, result


new = Deque()
new.main()
