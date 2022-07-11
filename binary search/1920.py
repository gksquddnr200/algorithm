import sys
input = sys.stdin.readline

N = int(input())
data1 = list(map(int,input().split()))

M = int(input())
data2 = list(map(int,input().split()))

data1.sort()

def recursion(i,start,end):
  if start > end:
    return 0
  middle = (start+end)//2
  if i == data1[middle]:
    return 1
  elif i > data1[middle]:
    return recursion(i,middle+1,end)
  else:
    return recursion(i,start,middle-1)

for i in data2:
  start = 0
  end = N-1
  print(recursion(i,start,end))