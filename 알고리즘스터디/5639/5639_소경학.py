import sys
sys.setrecursionlimit(10**6)
def DFS(start, end):
    if start > end:
        return
    now = end + 1
    for i in range(start + 1, end + 1):
        if graph[start] < graph[i]:
            now = i
            break
    DFS(start + 1, now - 1) 
    DFS(now, end)
    print(graph[start])
graph = []
while True:
    try:
        graph.append(int(sys.stdin.readline()))
    except:
        break
DFS(0, len(graph) - 1)