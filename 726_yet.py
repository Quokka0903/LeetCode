import sys

input = sys.stdin.readline

N = int(input())
hweui = []
for i in range(N):
    s, e = map(int, input().split())
    hweui.append([s, e])

hweui.sort(key= lambda x : (x[1], x[0]))

#print(hweui)

cnt = 1
end = hweui[0][1]
for i in range(1, N):
    if hweui[i][0] >= end:
        cnt += 1
        end = hweui[i][1]

print(cnt)