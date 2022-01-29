# Chap5: DFS/BFS

<aside>
📌 Stack : FILO, 박스 쌓기 → array의 append 및 pop으로 간단히 구현 가능
```swift
```python
stack.append(1)
stack.pop
```
```swift

Queue: FIFO, 대기줄 → collections의 deque 라이브러리로 구현
```swift
```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
queue.popleft()
queue.pop()
#결과값: 5 -> 5-2 -> 5-2-7 -> 2-7 -> 2
```
```swift

</aside>

<aside>
📌 Recursive function : 재귀 함수, 함수 자체가 자신을 call → **점화식**

Recursive function termination:
```swift
```python
def recursive(i):
	if i == 100:
		return
	recursive(i+1)		
```
```swift

</aside>

<aside>
📌 Graph 표현 방식:
1. Adjacency Matrix 인접 행렬

```swift
```python
INF = 999999999 # define infinite number

graph = [
		[0, 7 , 5]
		[7, 0, INF]
		[5, INF, 0]
]
```
```swift


2. 인접 리스트 Adjacency List
    
    
```swift
```python
#행이 3개인 2차원 리스트로 표현
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
...
graph[2].append((0,5))
```

1. 속도 disadvantage ⭐️

인접 행렬: 모든 관계를 저장하므로 노드 개수가 많을수록 메모리적으로 불리

인접 리스트: 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도 느림

</aside>

<aside>
📌 DFS : 깊이 우선 탐색→ 그래프에서 깊은 부분을 우선적으로 탐색함(최대한 먼) → O(N)
[ 알고리즘: Stack 자료 구조로 간단 구현(선입후출) ]

```python
def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: 
            dfs(graph, i ,visited)
```

BFS : 너비 우선 탐색→ 가까운 노드부터 탐색 → O(N)
[알고리즘: 1. 시작노드 큐에 삽입 후 방문 처리 → 2. 큐에서 노드를 꺼내 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 → 3. 끝까지 반복]

```python
from collections import deque

def bfs(graph, v, visited):
	queue = deque([v])
	visited[v] = True #1
	
	while queue: #3
		n = queue.popleft()#2-1
		for i in graph[n]:
			if not visited[i]:#2-2
				queue.append(i) #2-3
				visited[i] = True #2-4		
```

</aside>
```swift
