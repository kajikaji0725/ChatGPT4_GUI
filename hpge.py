import flet as ft

class Square(ft.UserControl):
    def build(self):
        return ft.ElevatedButton(
            '',
            width = 30,
            height = 30,
            bgcolor = ft.colors.BLUE_100,
            style = ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                padding = 1,
            ),
            on_click = self.on_click_handler,
        )

    def on_click_handler(self, e):
        e.control.text = 'X'
        self.update()


class Board(ft.UserControl):
    def renderSquare(self, i):
        return Square() 

    def build(self):
        return ft.Column(
            controls = [
                ft.Text(
                    'Next player: X'
                ),
                ft.Row(
                    controls=[
                        self.renderSquare(0),
                        self.renderSquare(1),
                        self.renderSquare(2),
                    ]
                ),
                ft.Row(
                    controls=[
                        self.renderSquare(3),
                        self.renderSquare(4),
                        self.renderSquare(5),
                    ]
                ),
                ft.Row(
                    controls=[
                        self.renderSquare(6),
                        self.renderSquare(7),
                        self.renderSquare(8),
                    ]
                ),
            ]
        )


class Game(ft.UserControl):
    def build(self):
        todo = ft.ListView()

        return ft.Column(
            width=100,
            controls = [
                Board(),
                ft.Text(''),
                todo,
            ]
        )


def main(page: ft.Page):
    set_page(page)

    page.add(
        Game()
    )

    page.update()


def set_page(page: ft.Page):
    page.window_width = 400
    page.window_height = 400
    page.window_left = 100
    page.window_top = 100
    page.horizontal_alignment = "center"

    page.theme_mode = ft.ThemeMode.LIGHT
    
ft.app(target=main)