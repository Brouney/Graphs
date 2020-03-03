import structures.adjacency_list as adj_list
import structures.adjacency_matrix as adj_matrix

import numpy


class IncidenceMatrix:
    def __init__(self):
        pass

    def from_file(self, file_path):
        self.matrix = numpy.loadtxt(file_path, int)

    def init_empty(self, nr_of_vertices):
        self.matrix = numpy.empty((nr_of_vertices, 0), int)

    def __str__(self):
        return str(self.matrix)

    def to_string(self):
        return str(self.matrix)

    def add_edge(self, vertex_1, vertex_2):
        nr_of_vertices = len(self.matrix)
        self.matrix = numpy.c_[self.matrix, numpy.zeros(nr_of_vertices, int)]

        self.matrix[vertex_1][-1] = 1
        self.matrix[vertex_2][-1] = 1

    def get_neighbors(self, vertex):
        neighbors = numpy.where(self.matrix[vertex] == 1)
        return neighbors[0]

    def to_adjacency_matrix(self):
        pass

    def to_adjacency_list(self):
        pass
