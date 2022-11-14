def bfs(i):
    queue = [] # 큐 선언 (리스트로 큐 구현)
    visited[i] = True
    queue.append(i) # 큐에 시작정점 삽입
    while len(queue) != 0:
        v = queue.pop(0) # 큐에서 정점 v를 가져옴
        print(v, end=' ') # 정점 v 출력
        for w in range(1, ver+1): # 정점 v에 인접한 방문 안된 정점에 대해
            if adj_list[v][w] and not visited[w]:
                visited[w] = True
                queue.append(w) # v에 인접한 정점을 큐에 삽입

ver, edge, s = map(int,input().split()) # 정점의 개수, 간선의 개수, 탐색 시작 정점 입력
adj_list = [[0] * (ver+1) for _ in range(ver+1)] # 그래프 인접행렬 생성
N = len(adj_list)
visited = [None] * N # 정점 방문 초기화

for _ in range(edge): # 무방향 그래프 인접행렬 생성
    a, b = map(int,input().split())
    adj_list[a][b] = 1
    adj_list[b][a] = 1

bfs(s)

