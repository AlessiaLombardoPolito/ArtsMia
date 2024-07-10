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
        self._view._page.update()