import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddGenere = None
        self._btnCreaGrafo = None
        self._ddAttore = None
        self._btnAttoriSimili = None
        self._txtGiorni = None
        self._btnSimulazione = None
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
        self._title = ft.Text("Simulazione d'esame 10/06/2020", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddGenere = ft.Dropdown(label="Genere (g)")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._ddGenere, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._controller.fillDDGeneri()

        # ROW2
        self._ddAttore = ft.Dropdown(label="Attore (a)")
        self._btnAttoriSimili = ft.ElevatedButton(text="Attori simili",
                                                  on_click=self._controller.handleAttoriSimili)

        row2 = ft.Row([
            ft.Container(self._ddAttore, width=300),
            ft.Container(self._btnAttoriSimili, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtGiorni = ft.TextField(label="#Giorni (n)")
        self._btnSimulazione = ft.ElevatedButton(text="Simulazione",
                                                 on_click=self._controller.handleSimulazione)
        row3 = ft.Row([
            ft.Container(self._txtGiorni, width=300),
            ft.Container(self._btnSimulazione, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

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
