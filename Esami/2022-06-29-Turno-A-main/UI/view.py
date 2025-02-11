import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddyear = None
        self.ddcountry = None
        self.txtN = None

        self.btn_graph = None
        self.btn_volume = None
        self.btn_path = None

        self.txt_result = None
        self.txtOut2 = None
        self.txtOut3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 29/06/2022 TURNO A iTunes", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.txtNCanzoni = ft.TextField(label="Numero canzoni")
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)

        row1 = ft.Row([self.txtNCanzoni, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.ddAlbum_a1 = ft.Dropdown(label="Album a1")
        self.btn_adiacenti = ft.ElevatedButton(text="Stampa adiacenze", on_click=self._controller.handle_adiacenti)
        row2 = ft.Row([self.ddAlbum_a1, self.btn_adiacenti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.ddAlbum_a2 = ft.Dropdown(label="Album a2")
        self.btn_percorso = ft.ElevatedButton(text="Stampa percorso", on_click=self._controller.handle_percorso)
        row3 = ft.Row([self.ddAlbum_a2, self.btn_percorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self.txtSoglia = ft.TextField(label="Soglia x")
        row4 = ft.Row([self.txtSoglia], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        self.txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut)
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
