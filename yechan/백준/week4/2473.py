import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.read

def three_search(n, data):
    data.sort()
    closest_sum = float('inf')
    result = []
    
    for i in range(n - 2):
        left, right = 0, n - 1
        
        while left < right:
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue

            current_sum = data[i] + data[left] + data[right]
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = [data[i], data[left], data[right]]
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return sorted([data[i], data[left], data[right]])
    
    return sorted(result)

input_data = input().split()
n = int(input_data[0])
data = list(map(int, input_data[1:]))

result = three_search(n, data)

print(' '.join(map(str, result)))



