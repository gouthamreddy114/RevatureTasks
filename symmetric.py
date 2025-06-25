m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
result = a ^ b
for num in sorted(result):
    print(num)