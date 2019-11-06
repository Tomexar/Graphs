
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    
class Graph:
    ''' 
    Represent a graph as a dictionary of vertices mapping labels to edges
    '''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            # Error
            pass
    def add_edge(self, vertex_from, vertex_to):
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            # Error
            pass


def earliest_ancestor(ancestors, starting_node):
    # Make a graph
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

        # add edges
        g.add_edge(pair[1], pair[0])

    # Traverse the graph with BFS
    q = Queue()
    q.enqueue([starting_node])    

    max_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        node = path[-1]

        # We keep the path if it's longer OR 
        if ((len(path) > max_path) or (len(path) == max_path and node < earliest_ancestor)):
            earliest_ancestor = node 
            max_path = len(path)

        for neighbors in g.vertices[node]:
            new_path = list(path)
            new_path.append(neighbors)
            q.enqueue(new_path)

    return earliest_ancestor