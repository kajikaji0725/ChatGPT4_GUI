import flet as ft
import time
from math import pi
from chatgpt4_gui import QuestionComponent

def main(page: ft.Page):
    
    def page_resize(e):
        print("New page size:", page.window_width, page.window_height)
    print(vars(page.on_resize))
    page.on_resize = page_resize
    print(vars(page.on_resize))
    
    page.update()
    
ft.app(target=main)








# これを使おう
# ft.ListView(expand=True, spacing=10)

# def main(page: ft.Page):
    
#     first_name = ft.Ref[ft.TextField]()
#     last_name= ft.Ref[ft.TextField]()
#     greetings = ft.Ref[ft.Column]()
    
#     def btn_click(e):
#         greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
#         first_name.current.value = ""
#         last_name.current.value = ""
#         page.update()
#         first_name.current.focus()
    
#     page.add(
#         ft.TextField(ref=first_name, label="First name", autofocus=True),
#         ft.TextField(ref=last_name, label="Last name"),
#         ft.ElevatedButton("Say hello!", on_click=btn_click),
#         ft.Column(ref=greetings)
#     )

# page.scroll = ft.ScrollMode.AUTO
#     def on_scroll(e: ft.OnScrollEvent):
#         if e.pixels >= e.max_scroll_extent - 100:
#             if sem.acquire(blocking=False):
#                 try:
#                     for i in range(0, 10):
#                         cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i),expand=True))
#                         s.i += 1
#                     cl.update()
#                 finally:
#                     sem.release()

#     cl = ft.Column(
#         spacing=ft.alignment.center,
#         height=100,
#         width=200,
#         scroll=ft.ScrollMode.ALWAYS,
#         # alignment=ft.alignment.
#         # on_scroll_interval=0,
#         # on_scroll=on_scroll,
#     )
#     # for i in range(0, 50):
#     #     cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))
#     #     s.i += 1
    
    
#     page.add(
#         ft.Container(cl,alignment=ft.alignment.center),
#         ft.TextField()
#     )
    
