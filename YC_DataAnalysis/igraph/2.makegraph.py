import igraph
print(igraph.__version__) #版本

graph1 = igraph.Graph([(0,2),(0,3),(3,1),(3,4),(3,5),(1,4)])
print(graph1)
print(graph1.degree()) #每个点与其他几个点有关系
print('-------------')
print(igraph.summary(graph1))
igraph.plot(graph1)
igraph.Graph.community_walktrap