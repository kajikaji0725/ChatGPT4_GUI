from chatgpt4_gui import View
import flet as ft


class Setting(ft.UserControl):
    def __init__(self, view: View):
        super().__init__()
        self.view = view
        self.stream = True
        self.is_use_history = False
        self.model = "gpt-3.5-turbo"
        self.temp = 0
        self.checkBox_gpt_3_5 = ft.Checkbox(
            label="gpt-3.5-turbo", value=self.model == "gpt-3.5-turbo", on_change=self.chenge_chatGPT_mode)
        self.checkBox_gpt_4 = ft.Checkbox(
            label="gpt-4", value=self.model == "gpt-4", on_change=self.chenge_chatGPT_mode)

        self.checkBox_strem = ft.Checkbox(
            label="strem", value=self.stream, on_change=self.chenge_restrem)
        self.checkBox_is_use_history = ft.Checkbox(
            label="is_use_history", value=self.is_use_history, on_change=self.chenge_is_use_history
        )

        self.page = view.getter_page()
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("注意"),
            content=ft.Text("設定，会話履歴などを初期化します．本当に大丈夫ですか？"),
            actions=[
                ft.TextButton("Yes", on_click=self.close_dialog_initialize),
                ft.TextButton("No", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def build(self):
        return ft.Column(controls=[
            self.checkBox_strem,
            self.checkBox_is_use_history,
            ft.Row(controls=[
                ft.Text("ChatGPT_mode"),
                self.checkBox_gpt_3_5,
                self.checkBox_gpt_4,
            ]), ft.FilledButton("初期化", on_click=self.open_dialog)
        ])

    def setter_initialize(self):
        self.stream = True
        self.is_use_history = False
        self.model = "gpt-3.5-turbo"
        self.temp = 0
        self.checkBox_gpt_3_5.value = self.model == "gpt-3.5-turbo"
        self.checkBox_gpt_4.value = self.model == "gpt-4"
        self.checkBox_strem.value = self.stream
        self.checkBox_is_use_history.value = self.is_use_history
        self.update()

    def close_dialog_initialize(self, e):
        self.dialog.open = False
        self.view.setter_config_initialize()
        self.setter_initialize()
        self.page.update()

    def close_dialog(self, e):
        self.dialog.open = False
        self.page.update()

    def open_dialog(self, e):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def setter_stream(self):
        self.view.setter_strem(self.stream)

    def setter_gpt_model(self):
        self.view.setter_gpt_model(self.model)

    def setter_is_use_history(self):
        self.view.setter_is_use_history(self.is_use_history)

    def chenge_restrem(self, e):
        self.stream = e.data
        self.setter_stream()

    def chenge_is_use_history(self, e):
        self.is_use_history = e.data
        self.setter_is_use_history()

    def chenge_chatGPT_mode(self, e):
        self.model = e.page._index[str(e.target)].label
        self.checkBox_gpt_3_5.value = self.model == "gpt-3.5-turbo"
        self.checkBox_gpt_4.value = self.model == "gpt-4"
        self.view.setter_gpt_model(self.model)
        self.update()
