import geopy.distance

from Lezioni.MetroParis.database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f
        self._linee = DAO.getAllLinee()
        self._lineaMap = {}
        for l in self._linee:
            self._lineaMap[l.id_linea] = l

    def getBestPath(self, v0, v1):
        costoTot, path = nx.single_source_dijkstra(self._grafo, v0, v1)
        return costoTot, path

    def getBFSNodes(self, source):
        edges = nx.bfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgeMode3()

    def buildGraphPesato(self):
        """Questo metodo e del tutto equivalente a buildGraph, ma chiama come metodo per aggiungere gli archi
        "addEdgePesati"""
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgePesati()

    def addEdgePesati(self):
        """Questo metodo assegna come peso degli edges il numero di linee che congiungono i diversi nodi.
        """
        self._grafo.clear_edges()
        allConnessioni = DAO.getAllConnessioni()
        for c in allConnessioni:
            v0 = self._idMap[c.id_stazP]
            v1 = self._idMap[c.id_stazA]
            linea = self._lineaMap[c.id_linea]
            peso = self.getTraversalTime(v0, v1, linea)
            if self._grafo.has_edge(v0, v1):
                if self._grafo[v0][v1]['weight'] > peso:
                    self._grafo[v0][v1]['weight'] = peso
            else:
                self._grafo.add_edge(v0, v1, weight=peso)

            # if self._grafo.has_edge(self._idMap[c.id_stazP],
            #                         self._idMap[c.id_stazA]):
            #     self._grafo[self._idMap[c.id_stazP]][self._idMap[c.id_stazA]]["weight"] += 1
            # else:
            #     self._grafo.add_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA], weight=1)

    def addEdgeMode3(self):
        """Mode 3: unica query che legge tutte le connessioni
        """
        self._grafo.clear_edges()
        allConnessioni = DAO.getAllConnessioni()
        # print(len(allConnessioni))
        for c in allConnessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            # print(f"Added edge between {u_nodo} and {v_nodo}")

    def addEdgeMode2(self):
        """Mode 2: loop singolo sui nodi e query per identificare i vicini
        """
        self._grafo.clear_edges()
        for u in self._fermate:
            vicini = DAO.getEdgesVicini(u)
            for v in vicini:
                v_nodo = self._idMap[v.id_stazA]
                self._grafo.add_edge(u, v_nodo)
                # print(f"Added edge between {u} and {v_nodo}")

    def addEdgeMode1(self):
        """Mode 1: doppio loop su nodi e query per ogni arco.
        """
        self._grafo.clear_edges()
        for u in self._fermate:
            for v in self._fermate:
                res = DAO.getEdge(u, v)
                if len(res) > 0:
                    self._grafo.add_edge(u, v)
                    # print(f"Added edge between {u} and {v}")

    def getArchiPesoMaggiore(self):
        """Print di archi con peso maggiore di 1 (agisce solo sul grafo pesato)
        """
        if len(self._grafo.edges) == 0:
            print("Il grafo è vuoto")
            return

        edges = self._grafo.edges
        result = []

        for u, v in edges:
            peso = self._grafo[u][v]["weight"]
            if peso > 1:
                result.append((u, v, peso))
        return result

    def getEdgeWeight(self, v1, v2):
        return self._grafo[v1][v2]["weight"]

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getTraversalTime(self, v0, v1, linea):
        p0 = (v0.coordX, v0.coordY)
        p1 = (v1.coordX, v1.coordY)
        dist = geopy.distance.distance(p0, p1).km
        vel = linea.velocita
        tempo = dist / vel * 60
        return tempo
