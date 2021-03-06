# Chap5: DFS/BFS

<aside>
๐ Stack : FILO, ๋ฐ์ค ์๊ธฐ โ array์ append ๋ฐ pop์ผ๋ก ๊ฐ๋จํ ๊ตฌํ ๊ฐ๋ฅ
```swift
```python
stack.append(1)
stack.pop
```
```swift

Queue: FIFO, ๋๊ธฐ์ค โ collections์ deque ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ก ๊ตฌํ
```swift
```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
queue.popleft()
queue.pop()
#๊ฒฐ๊ณผ๊ฐ: 5 -> 5-2 -> 5-2-7 -> 2-7 -> 2
```
```swift

</aside>

<aside>
๐ Recursive function : ์ฌ๊ท ํจ์, ํจ์ ์์ฒด๊ฐ ์์ ์ call โ **์ ํ์**

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
๐ Graph ํํ ๋ฐฉ์:
1. Adjacency Matrix ์ธ์  ํ๋ ฌ

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


2. ์ธ์  ๋ฆฌ์คํธ Adjacency List
    
    
```swift
```python
#ํ์ด 3๊ฐ์ธ 2์ฐจ์ ๋ฆฌ์คํธ๋ก ํํ
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
...
graph[2].append((0,5))
```

1. ์๋ disadvantage โญ๏ธ

์ธ์  ํ๋ ฌ: ๋ชจ๋  ๊ด๊ณ๋ฅผ ์ ์ฅํ๋ฏ๋ก ๋ธ๋ ๊ฐ์๊ฐ ๋ง์์๋ก ๋ฉ๋ชจ๋ฆฌ์ ์ผ๋ก ๋ถ๋ฆฌ

์ธ์  ๋ฆฌ์คํธ: ํน์ ํ ๋ ๋ธ๋๊ฐ ์ฐ๊ฒฐ๋์ด ์๋์ง์ ๋ํ ์ ๋ณด๋ฅผ ์ป๋ ์๋ ๋๋ฆผ

</aside>

<aside>
๐ DFS : ๊น์ด ์ฐ์  ํ์โ ๊ทธ๋ํ์์ ๊น์ ๋ถ๋ถ์ ์ฐ์ ์ ์ผ๋ก ํ์ํจ(์ต๋ํ ๋จผ) โ O(N)
[ ์๊ณ ๋ฆฌ์ฆ: Stack ์๋ฃ ๊ตฌ์กฐ๋ก ๊ฐ๋จ ๊ตฌํ(์ ์ํ์ถ) ]

```python
def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: 
            dfs(graph, i ,visited)
```

BFS : ๋๋น ์ฐ์  ํ์โ ๊ฐ๊น์ด ๋ธ๋๋ถํฐ ํ์ โ O(N)
[์๊ณ ๋ฆฌ์ฆ: 1. ์์๋ธ๋ ํ์ ์ฝ์ ํ ๋ฐฉ๋ฌธ ์ฒ๋ฆฌ โ 2. ํ์์ ๋ธ๋๋ฅผ ๊บผ๋ด ์ธ์  ๋ธ๋ ์ค ๋ฐฉ๋ฌธํ์ง ์์ ๋ธ๋๋ฅผ ๋ชจ๋ ํ์ ์ฝ์ํ๊ณ  ๋ฐฉ๋ฌธ์ฒ๋ฆฌ โ 3. ๋๊น์ง ๋ฐ๋ณต]

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
