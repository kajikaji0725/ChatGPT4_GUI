from .Question import Question
from .Talking import Talking
from dotenv import load_dotenv
import flet as ft
import os


class View(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.question = Question(self.send_click)
        self.talking = Talking()
        self.page = page 
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("注意"),
            content=ft.Text("会話履歴を初期化します．保存は大丈夫ですか？"),
            actions=[
                ft.TextButton("Yes", on_click=self.close_dialog_initialize),
                ft.TextButton("No", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        if os.path.isfile(".env"):
            load_dotenv()
            self.talking.setter_API_key(os.getenv("CHATGPT4_APIKEY"))

        else:
            return 0

    def build(self):
        return ft.Column(
            controls=[
                self.talking,
                self.question
            ],
        )

    def close_dialog_initialize(self, e):
        self.dialog.open = False
        self.talking.setter_histrory_initialize()
        self.page.update()

    def close_dialog(self, e):
        self.dialog.open = False
        self.page.update()

    def open_dialog(self, e):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def setter_config_initialize(self):
        self.talking.setter_config_initialize()

    def setter_strem(self, strem):
        self.talking.setter_stream(strem)

    def setter_gpt_model(self, model):
        self.talking.setter_gpt_model(model)

    def setter_is_use_history(self, is_use_history):
        self.talking.setter_is_use_history(is_use_history)

    def getter_page(self):
        return self.page

    def getter_chatmessage(self):
        return self.talking.getter_chatmessage()

    def getter_config_info(self):
        return self.talking.getter_config_infomation()

    def resize(self, e):
        # print(f"{e.data.split(',')}")
        data = e.data.split(',')
        self.talking.resize(int(float(data[1])), int(float(data[0])))
        self.update()

    def config(self, e):
        print(vars(e.control))

    def send_click(self, question):
        self.talking.setter_question(question)
        # self.talkingComponent.setter(word)

    def save_file_result(self, e: ft.FilePickerResultEvent):
        self.save_path = e.path if e.path else "Cancelled!"
        self.download_talking()

    def download_talking(self):
        text = []
        for i in self.talking.getter_cl().controls:
            text.append(i._Control__attrs['value'][0])

        with open(f'{self.save_path}.txt', 'w',encoding='UTF-8') as f:
            f.write(str(self.talking.getter_config_infomation())+'\n')
            f.writelines([txt+'\n' for txt in text])
