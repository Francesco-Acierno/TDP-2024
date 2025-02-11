import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddProvider = None
        self._btnCreaGrafo = None
        self._txtDistanza = None
        self._btnAnalisiGrafo = None
        self._txtStringa = None
        self._btnCalcolaPercorso = None
        self._ddTarget = None
        self.txt_result = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 18/01/2023 NYC-Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1

        self._ddProvider = ft.Dropdown(label="Provider", on_change=self.controller.getSelectedProvider)
        self._controller.fillDDProvider()
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._ddProvider, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._txtDistanza = ft.TextField(label="Distanza")
        self._btnAnalisiGrafo = ft.ElevatedButton(text="Analisi Grafo",
                                                  on_click=self._controller.handleAnalisiGrafo)

        row2 = ft.Row([
            ft.Container(self._txtDistanza, width=300),
            ft.Container(self._btnAnalisiGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtStringa = ft.TextField(label="Stringa")
        self._btnCalcolaPercorso = ft.ElevatedButton(text="Calcola Percorso",
                                                     on_click=self._controller.handleCalcolaPercorso)
        row3 = ft.Row([
            ft.Container(self._txtStringa, width=300),
            ft.Container(self._btnCalcolaPercorso, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._ddTarget = ft.Dropdown(label="Target")
        row4 = ft.Row([
            ft.Container(self._ddTarget, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
