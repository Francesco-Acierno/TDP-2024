import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def getForme(self, anno):
        return DAO.getAllForme(anno)

    def buildGraph(self, anno, forma):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodi())
        for n in self.grafo.nodes:
            self._idMap[n.id] = n

        confini = DAO.getPaeseiConfinanti(self._idMap)
        for b in confini:
            self.grafo.add_edge(b.c1, b.c2)
            self.grafo[b.c1][b.c2]["weight"] = DAO.getPeso(anno, forma, b.c1.id, b.c2.id)

    def getAdiacenti(self):
        vicini = {}
        for n in self.grafo.nodes:
            peso = 0
            for v in self.grafo.neighbors(n):
                peso += self.grafo[n][v]["weight"]
            vicini[n] = peso
        return vicini


