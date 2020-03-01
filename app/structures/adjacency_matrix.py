class AdjacencyMatrix:
    def __init__(self):
        self.graph = []
        self.size = 0

    def from_string(self, data_string):
        for line in iter(data_string.splitlines()):
            line = ''.join(line.split())
            self.graph.append(line.split('|'))

        self.size = len(self.graph[0])

    def to_string(self):
        result = ''
        for row in self.graph:
            result += str(row) + '\n'
        return result

    def add_edge(self, vertex_1, vertex_2):
        self.graph[vertex_1][vertex_2] = '1'
        self.graph[vertex_2][vertex_1] = '1'

    def get_neighbors(self, vertex):
        return [i for i, elem in enumerate(self.graph[vertex]) if elem == '1']