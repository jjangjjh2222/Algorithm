def dfs(v):
    visited[v] = True # 정점 v 방문
    print(v, end = '\n') # 정점 v 출력
    adj_list[v].sort()
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]: 
            dfs(w) # v에 인접한 방문 안된 정점 재귀호출

ver, edge, s = map(int,input().split())
adj_list = [[-1]] + [[] for _ in range(ver)]
N = len(adj_list) 
visited = [None] * N

for _ in range(edge):
    a, b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
 

dfs(s)

