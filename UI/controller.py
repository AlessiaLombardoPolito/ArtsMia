import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNUmNodes()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))
        self._view._page.update()

    def handleCompConnessa(self,e):
        global intId
        idAdded = self._view._txtIdOggetto.value

        try:
            intId = int(idAdded)

        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero"))
            self._view._page.update()

        if self._model.checkExistence(intId):
            self._view.txt_result.controls.append(ft.Text(f"l'oggetto con id {intId} è presente nel grafo"))

        else :
            self._view.txt_result.controls.append(ft.Text(f"l'oggetto con id {intId} non esiste nel grafo"))

        comp = self._model.getConnessa(intId)
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {intId} ha dimensione {comp}"))


        #riempio il dd
        self._view._ddLun.disabled = False
        self._view._btnCercaPercorso.disabled = False
        myOpts = list(range(2, comp))
        myOptsDD = list(map(lambda x: ft.dropdown.Option(x), myOpts))
        self._view._ddLun.options = myOptsDD

        """alternativa se non so usare lambda
        for i in range(2, comp):
            self._view._ddLun.options.append(ft.dropdown.Option(i)"""

        self._view._page.update()


    def handleCercaPercorso(self, e):
        lista, costo = self._model.getBestPath(int(self._view._ddLun.value), self._model.getObjFromId(int(self._view._txtIdOggetto.value)))

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"percorso trovato con peso uguale a {costo}"))
        self._view.txt_result.controls.append(ft.Text(f"percorso :"))
        for p in lista:
            self._view.txt_result.controls.append(ft.Text(f"{p}"))


        self._view._page.update()


