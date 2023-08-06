from dotenv import load_dotenv
import openai
import os

load_dotenv()

KEY = os.getenv("CHATGPT4_APIKEY")
print(KEY)

openai.api_key = KEY

messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Who won the world series in 2020?"},
  {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
  {"role": "user", "content": "Where was it played?"}
]

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

print(completion)





#from flet import *

# def main(page: Page):
#     page.title = "Osaka ni Oide"

#     page.appbar = AppBar(title=Text("index"))
#     page.controls.append(ElevatedButton("Visit Doutonbori", on_click=lambda _: page.go("/doutonbori")))


#     def route_change(route):
#         if page.route == "/doutonbori":
#             page.views.append(
#                 View(
#                     "/doutonbori",
#                     [
#                         AppBar(title=Text("Doutonbori")),
#                         ElevatedButton("Search Takoyaki", on_click=lambda _: page.go("/doutonbori/takoyaki")),
#                     ],
#                 )
#             )

#         if page.route == "/doutonbori/takoyaki":
#             page.views.append(
#                 View(
#                     "/doutonbori/takoyaki",
#                     [
#                         AppBar(title=Text("Takoyaki")),
#                         Text("たこ焼き食べたい"),
#                     ],
#                 )
#             )
#         page.update()

#     def view_pop(view):
#         page.views.pop()
#         if len(page.views) > 1:
#             page.update()
#         else : page.go('/')

#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#     page.go(page.route)


# if __name__ == '__main__':
#     app(target=main)


# import threading
# import flet as ft
# import time

# def main(page: ft.Page):

#     def check_item_clicked(e):
#         e.control.checked = not e.control.checked
#         page.update()

#     page.window_min_width = 740
#     a = hoge()

#     page.add(a)
#     page.update()

#     pick_files_dialog = ft.FilePicker(on_result=a.save_file_result)
#     page.overlay.append(pick_files_dialog)

#     page.appbar = ft.AppBar(
#         leading=ft.Icon(ft.icons.PALETTE),
#         leading_width=40,
#         title=ft.Text("AppBar Example"),
#         center_title=False,
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         actions=[
#             ft.IconButton(ft.icons.SETTINGS,on_click=pick_files_dialog.save_file),
#             # ft.IconButton(ft.icons.FILTER_3),
#             # ft.PopupMenuButton(
#             #     items=[
#             #         ft.PopupMenuItem(text="Item 1"),
#             #         ft.PopupMenuItem(),  # divider
#             #         ft.PopupMenuItem(
#             #             text="Checked item", checked=False, on_click=check_item_clicked
#             #         ),
#             #     ]
#             # ),
#         ],
#     )

#     print(vars(page.on_resize))
#     page.on_resize = a.resize
#     print(vars(page.on_resize))

#     page.update()

# class hoge(ft.UserControl):
#     def __init__(self):
#         super().__init__()
#         self.hoge = hoge2()
#         self.save_path = ""

#     def build(self):
#         self.word = ft.TextField()
#         self.cl = ft.Column(spacing=ft.alignment.center,
#         height=100,
#         width=200,
#         scroll=ft.ScrollMode.ALWAYS,
#         )
#         self.task = ft.Column()

#         return ft.Column(
#             controls=[
#                 ft.Row(controls=[self.cl],
#                        alignment=ft.MainAxisAlignment.CENTER
#                        ),
#                 ft.Container(
#                     content=ft.Stack(
#                     [
#                         ft.Row(
#                             controls=[
#                                 self.hoge,
#                                 ft.IconButton(icon=ft.icons.HIDE_IMAGE,on_click=self.add_click),
#                             ],

#                         ),
#                     ]
#                 ),
#                     alignment=ft.alignment.bottom_center
#                     ),
#             ],
#         )

#     def add_click(self,e):
#         print(vars(e.control))
#         # print(self.hoge.getter())
#         aa = ft.Text()
#         # self.cl.controls.append(ft.Container(
#         #     content=ft.Text(self.hoge.getter()),
#         # ))
#         # self.cl.controls.append(aa)
#         self.cl.controls.append(aa)
#         for i in range(100):
#             if i != 0:
#                 aa.value = str(aa.value) + str(i)
#             else:
#                 aa.value = str(i)
#             self.update()

#         # self.task.controls.append(ft.Text(self.word.value))
#         self.word.value = ""
#         self.update()
#         # print(self.cl)

#     def save_file_result(self,e: ft.FilePickerResultEvent):
#         self.save_path = e.path if e.path else "Cancelled!"
#         self.download_talking()

#     def download_talking(self):
#         print(self.save_path)
#         text = []
#         for i in self.cl.controls:
#             text.append(i._Control__attrs['value'][0])

#         with open(f'{self.save_path}.txt','w') as f:
#             f.writelines([txt+'\n' for txt in text])

#         # pick_files_dialog.save_file()


#     def resize(self,e):
#         # print(f"{e.data.split(',')}")
#         data = e.data.split(',')
#         print(data)
#         self.cl.height = int(float(data[1])) - 150
#         self.cl.width = int(float(data[0])) - 200
#         self.update()


# class hoge2(ft.UserControl):
#     def __init__(self):
#         super().__init__()
#         self.word = ft.TextField(
#             multiline=True,
#             max_lines=4,
#             width=673,
#         )

#     def build(self):
#         return ft.Container(
#             content=self.word,
#             alignment=ft.alignment.center
#             )

#     def getter(self):
#         return self.word.value

#     def resize(self):
#         print("hoge")


# class hoge3:
#     def __init__(self) -> None:
#         pass

# ft.app(main)


# # これを使おう
# # ft.ListView(expand=True, spacing=10)

# # def main(page: ft.Page):

# #     first_name = ft.Ref[ft.TextField]()
# #     last_name= ft.Ref[ft.TextField]()
# #     greetings = ft.Ref[ft.Column]()

# #     def btn_click(e):
# #         greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
# #         first_name.current.value = ""
# #         last_name.current.value = ""
# #         page.update()
# #         first_name.current.focus()

# #     page.add(
# #         ft.TextField(ref=first_name, label="First name", autofocus=True),
# #         ft.TextField(ref=last_name, label="Last name"),
# #         ft.ElevatedButton("Say hello!", on_click=btn_click),
# #         ft.Column(ref=greetings)
# #     )

# # page.scroll = ft.ScrollMode.AUTO
# #     def on_scroll(e: ft.OnScrollEvent):
# #         if e.pixels >= e.max_scroll_extent - 100:
# #             if sem.acquire(blocking=False):
# #                 try:
# #                     for i in range(0, 10):
# #                         cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i),expand=True))
# #                         s.i += 1
# #                     cl.update()
# #                 finally:
# #                     sem.release()

# #     cl = ft.Column(
# #         spacing=ft.alignment.center,
# #         height=100,
# #         width=200,
# #         scroll=ft.ScrollMode.ALWAYS,
# #         # alignment=ft.alignment.
# #         # on_scroll_interval=0,
# #         # on_scroll=on_scroll,
# #     )
# #     # for i in range(0, 50):
# #     #     cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))
# #     #     s.i += 1


# #     page.add(
# #         ft.Container(cl,alignment=ft.alignment.center),
# #         ft.TextField()
# #     )
