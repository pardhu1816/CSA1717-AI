import heapq
G = [[1,2,3],[4,5,6],[7,8,0]]
P = {n:(i,j) for i,r in enumerate(G) for j,n in enumerate(r)}
class N:
  def __init__(s,S,p=None,g=0):s.S,S=s.h(S),S;s.p,p=s.f(s.S)+g,p;s.S,g=g,S
  def h(s,S):return sum(abs(i-P[n][0])+abs(j-P[n][1])for i,r in enumerate(S)for j,n in enumerate(r)if n)
  def f(s):return s.S
  def __lt__(a,b):return a.p<b.p
def a_star(S):
  O,C=[N(S)],set()
  while O:
    n=heapq.heappop(O)
    if n.S==G:return n
    C.add(str(n.S))
    i,j=[(i,j)for i in range(3)for j in range(3)if n.S[i][j]==0][0]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      x,y=i+dx,j+dy
      if 0<=x<3 and 0<=y<3:
        T=[r[:] for r in n.S]
        T[i][j],T[x][y]=T[x][y],T[i][j]
        if str(T) not in C:heapq.heappush(O,N(T,n,n.f()+1))
def path(n):
  R=[]
  while n:R.append(n.S);n=n.p
  return R[::-1]
S = [[1,2,3],[4,0,6],[7,5,8]]
for s in path(a_star(S)):print(*s,sep='\n');print()
