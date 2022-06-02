n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()
l=len(arr)
for i in range(2,l+2):
    if arr[l-1]>arr[l-i]:
        print(arr[l-i])
        break
