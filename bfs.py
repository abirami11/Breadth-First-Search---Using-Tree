def bfs(s, Adj):
	level = {s:0}
	parent = { s:None}
	i = 1
	frontier = [s]
	while frontier:
		next = []
		for u in frontier:
			print u
			for v in Adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
		frontier = next
		i += 1
	print level

Adj = { 'b':{'a','c'} , 'a':{'c'}, 'c':{'b'}}
s = 'b'
bfs(s,Adj)