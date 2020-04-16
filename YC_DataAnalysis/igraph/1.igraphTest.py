import igraph
print(igraph.__version__) #版本
graph1 = igraph.Graph(1)#最简单的图
print('-------------')
print(graph1)#图的对象
graph1.add_vertices(3) #增加3个顶点
print('-------------')
print(graph1)
graph1.add_edges([(0,1),(1,2),(0,2),(0,3),(1,3),(2,3)])  #增加6个边长
print('-------------')
print(graph1)
file = open('1.net','w')
graph1.write_pajek(file)
file.close()