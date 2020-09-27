class Vertex:
    def __init__(self,value):
        self.value = value
        self.distance = None
        self.pi = None
        self.visited = None

class PriorityQueue:
    def __init__(self):
        self.lst = []

    def isEmpty(self):
        if self.lst is []:
            return True
        return False

    def Enqueue(self,val):
        v = Vertex(val)
        self.lst.append(v)

    def Dequeue(self):
        self.lst.pop(v)

    def ExtractMin(self,source):
        if source == 0:
            min = self.lst[source+1]
        else:
            min = self.lst[source-1]
        for i in self.lst:
            if min.distance > i.distance and i.visited != True:
                min = i
        return min


class DGraph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.adj = [[0 for i in range(self.vertex)] for j in range(self.vertex)]
        self.Q = PriorityQueue()
        for i in range(self.vertex):
            self.AddQueue(i)

    def AddDirectedEdges(self,source,dest,cost):
        self.adj[source][dest] = cost

    def GetDirectedNeighbours(self,source):
        lst = []
        for i in range(self.vertex):
            if self.adj[source][i] != 0:
                lst.append(i)
        return lst

    def AddQueue(self,val):
        if len(self.Q.lst) <= self.vertex - 1:
            self.Q.Enqueue(val)

    def ReturnQueue(self):
        for i in self.Q.lst:
            print(i.value)
            print(i.distance)

    def Relax(self,u,v):
        pass

    def IntializeSingleSource(self,source):
        for i in self.Q.lst:
            if i.value != source:
                i.distance = float('inf')
            else:
                i.distance = 0

    def DijkstraShortestPath(self, source):
        self.IntializeSingleSource(source)
        S = []
        while len(S) != self.vertex:
            u = self.Q.ExtractMin(source)
            self.Q.lst[u.value].visited = True
            S.append(u)
            n = self.GetDirectedNeighbours(u.value)
            for i in n:
                if self.Q.lst[i].distance > self.Q.lst[u.value].distance + self.adj[u.value][i]:
                    self.Q.lst[i].distance = self.Q.lst[u.value].distance + self.adj[u.value][i]
                    self.Q.lst[i].pi = self.Q.lst[u.value].value
        for i in range(self.vertex):
            print("Node:{} Distance:{} Pi:{}".format(self.Q.lst[i].value,self.Q.lst[i].distance,self.Q.lst[i].pi))

d = DGraph(5)
d.AddDirectedEdges(0,1,10)
d.AddDirectedEdges(0,3,5)
d.AddDirectedEdges(1,2,1)
d.AddDirectedEdges(1,3,2)
d.AddDirectedEdges(2,4,4)
d.AddDirectedEdges(3,1,3)
d.AddDirectedEdges(3,2,9)
d.AddDirectedEdges(3,4,2)
d.AddDirectedEdges(4,0,7)
d.AddDirectedEdges(4,2,6)
d.DijkstraShortestPath(0)





