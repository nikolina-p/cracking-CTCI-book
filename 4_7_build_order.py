from collections import defaultdict


class Vertex:

    def __init__(self, name: str = None):
        self.name = name
        self.adjacent = []


def build_order(projects, dependencies):
    """
    4.7. Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
    projects, where the second project is dependent on the first project). Ail of a project's dependencies
    must be built before the project is. Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.
    """
    try:
        no_preceding = list(projects)  # keep track of projects that have no preceding projects [str]
        vertices = {name: Vertex(name) for name in projects}  # graph nodes(vertices)
        depends_on = defaultdict(list)  # dictionary of project(key): list of preceding projects(value)

        # build graph and find vertices(projects) that have no preceding projects (starting projects)
        for project in vertices:
            for dependency in dependencies:
                if project == dependency[0]:
                    vertices[project].adjacent.append(vertices[dependency[1]])  # add dependency
                    depends_on[dependency[1]].append(project)
                    if dependency[1] in no_preceding:
                        no_preceding.remove(dependency[1])  # remove dependency from preceding

        if not no_preceding:
            # if there are no projects that have no preceding projects return Error
            raise IndexError("No valid build order")

        # do the breath first traversal
        to_be_visited = [vertices[name] for name in no_preceding]
        visited = []
        while to_be_visited:
            # while there are elements in to_be_visited, take first one, check if it has preceding;
            # if yes, move to the next; if no - add it to visited and process adjacent vertices
            cycle = True
            for vx in to_be_visited:
                if not depends_on[vx.name]:
                    # if the project has no preceding projects - empty []
                    cycle = False
                    if vx not in visited:
                        visited.append(vx)
                        to_be_visited.remove(vx)
                        for adj in vx.adjacent:
                            if adj not in to_be_visited:
                                to_be_visited.append(adj)
                            depends_on[adj.name].remove(vx.name)  # remove visited node from all its dependencies
                    else:
                        raise IndexError(f"The {vx.name} already visited. The graph has cycle, no possible build order")
            # cycle will be True if all to_be_visited vertices depend on some other vertex
            if cycle:
                raise IndexError("Cycle. No valid build order")

        if len(visited) == len(projects):
            return visited
        else:
            raise IndexError("No valid build order.")
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print([vx.name for vx in build_order(projects, dependencies)])

    # with cycle
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('c', 'b')]
    bo = build_order(projects, dependencies)

    # book test case
    projects_book = ["a", "b", "c", "d", "e", "f", "g"]
    dep_book = [('f', 'b'), ('f', 'c'), ('f', 'a'), ('c', 'a'), ('b', 'a'), ('b', 'e'), ('a', 'e'), ('d', 'g')]
    print([vx.name for vx in build_order(projects_book, dep_book)])

    """
    OUTPUT:
    ['e', 'f', 'b', 'a', 'd', 'c']
    Cycle. No valid build order
    ['d', 'f', 'g', 'c', 'b', 'a', 'e']
    """
