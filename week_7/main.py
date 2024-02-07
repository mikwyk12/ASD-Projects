import polska
from graph_class import *


def test_matrix():
    poland = GraphMatrix()

    for key1, key2 in polska.graf:
        v1 = Vertex(polska.slownik[key1])
        v2 = Vertex(polska.slownik[key2])
        poland.insert_edge(v1, v2)
    poland.delete_edge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
    poland.delete_edge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
    poland.delete_vertex(Vertex(polska.slownik['K']))
    polska.draw_map(poland.edges())


def test_list():
    poland = GraphList()
    for key1, key2 in polska.graf:
        v1 = Vertex(polska.slownik[key1])
        v2 = Vertex(polska.slownik[key2])
        poland.insert_edge(v1, v2)
    poland.delete_edge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
    poland.delete_edge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
    poland.delete_vertex(Vertex(polska.slownik['K']))
    polska.draw_map(poland.edges())


if __name__ == '__main__':
    test_matrix()
    test_list()
