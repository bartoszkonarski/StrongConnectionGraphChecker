class Graph:


    def __init__(self, edges,nodes):
        # Zamiana na postać liczbową w celu możliwości indeksacji w listach sąsiedztwa
        translator = {}
        current = 0
        for node in nodes:
            translator[node]=current
            current+=1
        self.edgesReformed = []
        for (start, end) in edges:
            self.edgesReformed.append((translator[start],translator[end]))
        # Utworzenie list sąsiedztwa
        self.n = len(translator)
        self.adjList = [[] for node in range(self.n)]
        for (start, end) in self.edgesReformed:
            self.adjList[start].append(end)
        print(self.adjList)

def DFS(graph, v, visited):
    visited[v] = True
    for listNumber in graph.adjList[v]:
        if not visited[listNumber]:
            DFS(graph, listNumber, visited)

def isGraphStronglyConnected(graph):
    N = graph.n
    for i in range(N):
        visited = [False for p in range(N)]
        DFS(graph, i, visited)
        for node in visited:
            if node == False:
                return False

    return True


if __name__ == '__main__':
    pass