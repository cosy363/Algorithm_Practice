# Chap4: Implementation

바둑판 배열의 움직임 implementation

→ 바둑판을 일일이 구현할 필요없이 이동 방향을 Array 형식으로 기록하여 공간을 벗어나는 경우 무시하도록 Code
```swift
```python
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
```
```swift

How to set get map data from grid input:
```swift
```python
array=[]
for i in range:
	array.append(list(map(int,input().split())))
```
```swift

바둑판 배열에서 움직임을 표현할 시 방법:

1. dx,dy를 각각 리스트로 선언하여 “nx = x +dx[i]” 형식으로 표현
2. dxdy를 한꺼번에 선언하여 “nx = x + dxdy[0]” 형식으로 표현

##