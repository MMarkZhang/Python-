
### 算法思路
使用了广度优先搜索解决赋权有向图或者无向图的单源最短路径问题，算法最终得到一个最短路径树。该算法常用于路由算法或者作为其他图算法的一个子模块。

Dijkstra算法采用的是一种**贪心的策略**，声明一个数组dis来保存源点到各个顶点的最短距离和一个保存已经找到了最短路径的顶点的**集合：T**，初始时，原点 s 的路径权重被赋为 0 （dis\[s] = 0）。若对于顶点 s 存在能直接到达的边（s,m），则把dis\[m]设为w（s, m）,同时把所有其他（s不能直接到达的）顶点的路径长度设为无穷大。初始时，集合T只有顶点s。 
然后，从dis数组选择最小值，则该值就是**源点s到该值对应的顶点的最短路径**，并且把该点加入到T中，OK，此时完成一个顶点， 
然后，我们需要看看新加入的顶点是否可以到达其他顶点并且看看通过该顶点到达其他点的路径长度是否比源点直接到达短，如果是，那么就替换这些顶点在dis中的值。 
然后，又从dis中找出最小值，重复上述动作，直到T中包含了图的所有顶点。

https://blog.csdn.net/qq_35644234/article/details/60870719

### 上述例子的图片表示
![路径图](https://66.media.tumblr.com/354c79e28e80291d39e85b4b39e774b9/tumblr_pfs52stuTA1vdexuso1_500.png)
![初始化](https://78.media.tumblr.com/881a9456c06fac376e0e4f765395e4fe/tumblr_pfs52stuTA1vdexuso2_1280.png)
![1](https://78.media.tumblr.com/c17454174ce79a50492930fbac11ceb2/tumblr_pfs52stuTA1vdexuso3_640.png)
![2](https://78.media.tumblr.com/d6310dea0db67d413f4bf88c11054208/tumblr_pfs52stuTA1vdexuso4_640.png)
![3](https://78.media.tumblr.com/f8e6f2ad93f53461692490d4adfd2c59/tumblr_pfs52stuTA1vdexuso5_640.png)
![4](https://78.media.tumblr.com/791c56a2337e3a26b0dde26d07ba054c/tumblr_pfs52stuTA1vdexuso6_1280.png)

### 实例和示范代码

**已知图例：**

![以此图为例](https://78.media.tumblr.com/6659ac55d031cdadf33b788977354a3c/tumblr_pfljnmZPVH1vdexuso1_1280.png)

**代码：**

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
输出：

```
[0, 5, 3, 6, 7, 9]
[0, 2, 0, 2, 2, 3]
```
**得到的最短路径：**

![粗线为路径](https://78.media.tumblr.com/2576215b57f2cb948f6de9f505b6f1fc/tumblr_pfok3hVEI81vdexuso1_640.png)
