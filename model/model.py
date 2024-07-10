from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        #slz 1 : successori di v0 in dfs
        successors = nx.dfs_successors(self._grafo, v0) #restituisce dizionario dei successori in una dfs
        allSuccessors = []
        for v in successors.values():
            allSuccessors.extend(v)


        #slz 2 : predecessori di v0 in dfs
        predecessors = nx.dfs_predecessors(self._grafo, v0)


        #slz 3 : conto i nodi dell'albero di visita del dfs
        albero = nx.dfs_tree(self._grafo, v0)

        #slz4 : node_connected_components
        connComp = nx.node_connected_component(self._grafo, v0)

        #il 3 e il 4 contengono anche il nodo di partenza, mentre il 2 e l'1 non lo contengono

        return(len(connComp))



    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        #self._grafo.edges.clear()

        #soluzione 1 : ciclare su tutti nodi
        """for u in self._artObjectList:
            for v in self._artObjectList:
                peso = DAO.getPeso(u, v)
                self._grafo.add_edge(u, v, weight = peso)"""

        #soluzione 2 : una sola query
        allEdges = DAO.getAllConnesioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weight=e.peso)
    def getNUmNodes(self):
        return len(self._grafo.nodes)


    def getNumEdges(self):
        return len(self._grafo.edges)

    def checkExistence(self, idOggetto):
        return idOggetto in self._idMap