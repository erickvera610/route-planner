from collections import deque
import heapq
def shortest_path(size,start,goal,blocked):
    if not isinstance(size,int) or not 2<=size<=40: raise ValueError('Grid size must be 2 to 40')
    start=tuple(start);goal=tuple(goal);blocked={tuple(p) for p in blocked}
    def valid(p):return len(p)==2 and all(isinstance(n,int) and 0<=n<size for n in p)
    if not valid(start) or not valid(goal) or any(not valid(p) for p in blocked):raise ValueError('Invalid coordinates')
    if start in blocked or goal in blocked:raise ValueError('Start and goal must be open')
    queue=deque([start]);parent={start:None}
    while queue:
        node=queue.popleft()
        if node==goal:
            path=[]
            while node is not None:path.append(list(node));node=parent[node]
            return {'path':path[::-1],'distance':len(path)-1,'visited':len(parent)}
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nxt=(node[0]+dx,node[1]+dy)
            if valid(nxt) and nxt not in blocked and nxt not in parent:parent[nxt]=node;queue.append(nxt)
    return {'path':[],'distance':None,'visited':len(parent)}
def dijkstra(graph,start,goal):
    if any(cost<0 for edges in graph.values() for _,cost in edges):raise ValueError('Nonnegative weights required')
    heap=[(0,start)];dist={start:0}
    while heap:
        cost,node=heapq.heappop(heap)
        if cost!=dist[node]:continue
        if node==goal:return cost
        for nxt,weight in graph.get(node,[]):
            value=cost+weight
            if value<dist.get(nxt,float('inf')):dist[nxt]=value;heapq.heappush(heap,(value,nxt))
    return None
def run(payload):return shortest_path(12,[0,0],[11,11],payload.get('blocked',[]))
