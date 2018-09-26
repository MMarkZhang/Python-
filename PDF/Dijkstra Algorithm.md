
![以此图为例](https://78.media.tumblr.com/6659ac55d031cdadf33b788977354a3c/tumblr_pfljnmZPVH1vdexuso1_1280.png)
代码：

```
=float('inf')
 
def dijkstra(graph,n):
	dis=[0]*n
	flag=[False]*n
	pre=[0]*n
	flag[0]=True
	k=0
	for i in range(n):
		dis[i]=graph[k][i]
 
	for j in range(n-1):
		mini=_
		for i in range(n):
			if dis[i]<mini and not flag[i]:
				mini=dis[i]
				k=i
		if k==0:#不连通
			return
		flag[k]=True
		for i in range(n):
			if dis[i]>dis[k]+graph[k][i]:
				dis[i]=dis[k]+graph[k][i]
				pre[i]=k
#		print(k)
	return dis,pre
 
if __name__=='__main__':
	n=6
	graph=[
			[0,6,3,_,_,_],
			[6,0,2,5,_,_],
			[3,2,0,3,4,_],
			[_,5,3,0,2,3],
			[_,_,4,2,0,5],
			[_,_,_,3,5,0],
			]
	dis,pre=dijkstra(graph,n)
	print(dis)
	print(pre)
```
