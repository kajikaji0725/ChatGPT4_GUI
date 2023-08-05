import flet as ft


class Question(ft.UserControl):
    def __init__(self, add_click, APIKey=None):
        super().__init__()
        self.word = ft.TextField(multiline=True,
                                 max_lines=3,
                                 width=673,)
        self.send_click = add_click

    def build(self):

        return ft.Container(ft.Stack(
            [
                ft.Row(
                    controls=[
                        self.word,
                        ft.IconButton(
                            icon=ft.icons.SEND, on_click=self.add_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ))

    def add_click(self, e):
        word = self.word.value
        self.word.value = ""
        self.update()
        self.send_click(word)
        