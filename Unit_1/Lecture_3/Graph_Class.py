"CLASS NODE"


class Node(object):
    def __init__(self, name):
        "Assumes name is a string"
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


"CLASS EDGE"


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.scr.getName() + "->" + self.dest.getName()


"CLASS DIGRAPH"


class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def children0f(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + "->" + dest.getName() + "\n"
        return result[:-1]  # omit final newline


"CLASS GRAPH"


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


"BUILD THE GRAPH"


def buildCityGraph(graphType):
    g = graphType()
    for name in (
        "Boston",
        "Providence",
        "New York",
        "Chicago",
        "Denver",
        "Phoenix",
        "Los Angeles",
    ):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("Providence")))
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("Boston")))
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("New York"), g.getNode("Chicago")))
    g.addEdge(Edge(g.getNode("Chicago"), g.getNode("Denver")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("Phoenix")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Los Angeles"), g.getNode("Boston")))
    return g


# print(buildCityGraph(Graph))


"EXERCISE 2"

# nodes = []
# nodes.append(Node("ABC"))  # nodes[0]
# nodes.append(Node("ACB"))  # nodes[1]
# nodes.append(Node("BAC"))  # nodes[2]
# nodes.append(Node("BCA"))  # nodes[3]
# nodes.append(Node("CAB"))  # nodes[4]
# nodes.append(Node("CBA"))  # nodes[5]

# g = Graph()

# for n in nodes:
#     g.addNode(n)
# g.addEdge(Edge(nodes[0], nodes[1]))
# g.addEdge(Edge(nodes[0], nodes[2]))
# g.addEdge(Edge(nodes[1], nodes[4]))
# g.addEdge(Edge(nodes[2], nodes[3]))
# g.addEdge(Edge(nodes[3], nodes[5]))
# g.addEdge(Edge(nodes[4], nodes[5]))

# print(g)


"FINDING THE SHORTEST PATH"


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
       path and shortest are lists of nodes
    Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print("Current DFS path:", printPath(path))
    if start == end:
        return path
    for node in graph.children0f(start):
        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print("Already visited", node)
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end ar nodes
    Returns a shortest path form strat to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp != None:
        print("Shortest path from", source, "to", destination, "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)


testSP("Chicago", "Boston")
testSP("Boston", "Phoenix")


def BFS(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; startand end are nodes
    Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print("Current BFS path", printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.children0f(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def shortestPath(graph, start, end, toPrint=False):
    """Assumes graph is a Digraph; start and end ar nodes
    Returns a shortest path form strat to end in graph"""
    return BFS(graph, start, end, toPrint)


testSP("Boston", "Phoenix")
