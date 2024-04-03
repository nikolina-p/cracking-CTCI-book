
class Vertex:

    def __init__(self, name: str, adjacent: list = None):
        self.name = name
        self.adjacent = adjacent if adjacent else []

    def add_adjacent(self, vertex: 'Vertex'):
        self.adjacent.append(vertex)

    def remove_adjacent(self, vertex: 'Vertex'):
        self.adjacent.remove(vertex)

    def is_adjacent(self, vertex: 'Vertex'):
        return vertex in self.adjacent

    def __str__(self):
        return self.name

    @staticmethod
    def are_connected_bft(v1: 'Vertex', v2: 'Vertex', visited: list = None, to_be_visited: list = None) ->bool:
        """Given a directed graph, design an algorithm to find out whether there is a route between two nodes."""
        if visited is None:
            visited = []

        if to_be_visited is None:
            to_be_visited = []

        current = v1
        visited.append(current)

        if v2 in current.adjacent:
            return True

        for adjacent in current.adjacent:
            if adjacent not in visited + to_be_visited:
                to_be_visited.append(adjacent)

        print(f"Current: {current}")
        print("Visited: ", [v.name for v in visited])
        print(f"To be visited: {[v.name for v in to_be_visited]}\n")

        if len(to_be_visited) > 0:
            next_current = to_be_visited[0]
            to_be_visited.remove(next_current)
        else:
            return False

        return Vertex.are_connected_bft(next_current, v2, visited, to_be_visited)

    @staticmethod
    def are_connected_dft(v1: 'Vertex', v2: 'Vertex', visited:list = None):
        if visited is None:
            visited = []

        current = v1
        visited.append(current)

        print(f"Current: {current}")
        print("Visited: ", [v.name for v in visited])

        if v2 in current.adjacent:
            return True

        for adjacent in current.adjacent:
            if adjacent not in visited:
                if Vertex.are_connected_dft(adjacent, v2, visited):
                    return True

        return False

if __name__ == "__main__":
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")

    h = Vertex("H")

    a.add_adjacent(b)
    a.add_adjacent(c)
    a.add_adjacent(d)

    b.add_adjacent(c)
    b.add_adjacent(e)

    c.add_adjacent(d)
    c.add_adjacent(e)

    d.add_adjacent(f)
    d.add_adjacent(g)

    e.add_adjacent(f)
    e.add_adjacent(g)

    f.add_adjacent(g)

    print("A -> ",[v.name for v in a.adjacent])
    print("B -> ",[v.name for v in b.adjacent])
    print("C -> ",[v.name for v in c.adjacent])
    print("D -> ",[v.name for v in d.adjacent])
    print("E -> ",[v.name for v in e.adjacent])
    print("F -> ",[v.name for v in f.adjacent])
    print("G -> ",[v.name for v in g.adjacent])

    #print("A to F? ",Vertex.are_connected_bft(a, f))
    #print("A to H? ", Vertex.are_connected_bft(a, h))

    print("A to F? ", Vertex.are_connected_dft(a, f))
    print("A to H? ", Vertex.are_connected_dft(a, h))
