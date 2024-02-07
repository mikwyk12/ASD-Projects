class Vertex:
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.key = data[2]

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class GraphMatrix:
    def __init__(self):
        self.matrix = []
        self.v_list = []
        self.index = {}
        self.size = 0

    def is_empty(self):
        return False if len(self.v_list) else True

    def get_vertex_idx(self, vertex):
        return self.index[vertex]

    def get_vertex(self, vertex_id):
        for key, value in self.index.items():
            if value == vertex_id:
                return key

    def insert_vertex(self, vertex):
        self.v_list.append(vertex)
        self.index[vertex] = len(self.v_list)-1
        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            for line in self.matrix:
                line.append(0)
            self.matrix.append([0 for i in range(len(self.matrix[0]))])

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.v_list.remove(vertex)
        self.index.pop(vertex)

        for i in range(len(self.v_list)):
            self.index[self.v_list[i]] = i

        self.matrix.pop(idx)
        for line in self.matrix:
            line.pop(idx)

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.v_list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.v_list:
            self.insert_vertex(vertex2)
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        self.matrix[idx1][idx2] = 1
        self.size += 1

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        self.matrix[idx1][idx2] = 0
        self.size -= 1

    def neighbours(self, vertex_idx):
        result = []
        for i in range(len(self.matrix[vertex_idx])):
            if self.matrix[vertex_idx][i] == 1:
                result.append(i)
        return result

    def size(self):
        return self.size

    def order(self):
        return len(self.matrix)

    def edges(self):
        result = []
        for row in range(len(self.matrix)):
            for col in range(row):
                if self.matrix[row][col] == 1:
                    result.append((self.get_vertex(row).key, self.get_vertex(col).key))
        return result


class GraphList:
    def __init__(self):
        self.list = []
        self.v_list = []
        self.index = {}
        self.size = 0

    def is_empty(self):
        return False if len(self.v_list) else True

    def get_vertex_idx(self, vertex):
        return self.index[vertex]

    def get_vertex(self, vertex_id):
        for key, value in self.index.items():
            if value == vertex_id:
                return key

    def insert_vertex(self, vertex):
        self.v_list.append(vertex)
        self.index[vertex] = len(self.v_list)-1
        self.list.append([])

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.v_list.remove(vertex)
        self.index.pop(vertex)

        for i in range(len(self.v_list)):
            self.index[self.v_list[i]] = i

        self.list.pop(idx)
        for line in self.list:
            if idx in line:
                line.remove(idx)
            for elem in line:
                if elem > idx:
                    idx -= 1

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.v_list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.v_list:
            self.insert_vertex(vertex2)
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        self.list[idx1].append(idx2)
        self.size += 1

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        self.list[idx1].remove(idx2)
        self.size -= 1

    def neighbours(self, vertex_idx):
        return self.list[vertex_idx]

    def size(self):
        return self.size

    def order(self):
        return len(self.list)

    def edges(self):
        result = []
        for i in range(len(self.list)):
            for elem in self.list[i]:
                result.append((self.get_vertex(i).key, self.get_vertex(elem).key))
        return result
