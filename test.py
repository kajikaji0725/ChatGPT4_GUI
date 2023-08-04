import threading
import flet as ft

def main(page: ft.Page):
    
    a = hoge()
    
    page.add(a)
    page.update()
    
    print(vars(page.on_resize))
    page.on_resize = a.resize
    print(vars(page.on_resize))
    # page.update()
    
    # def ee():
    #     print(a)
    # a = ft.TextField(on_change=ee())
    # page.add(a)

class hoge(ft.UserControl):
    def __init__(self):
        super().__init__()
        
    def page_resize(e):
        # self.cl.height = int(page.window_height) - 150
        # cl.width = int(page.width) - 200
        # page.update()
        print("New page size:", e)
      
    def build(self):
        self.word = ft.TextField()
        self.cl = ft.Column(spacing=ft.alignment.center,
        height=100,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,)
        self.task = ft.Column()
        
        for i in range(100):
            self.cl.controls.append(ft.Text(i))
        
        
        return ft.Column(
            controls=[
                self.cl,
                ft.Row(
                    controls=[
                        self.word,
                        ft.IconButton(icon=ft.icons.HIDE_IMAGE,on_click=self.add_click)
                    ]
                ),
            ]   
        )
        
    def add_click(self,e):
        self.cl.controls.append(ft.Text(self.word.value))
        self.task.controls.append(ft.Text(self.word.value))
        self.word.value = ""
        self.update()
        print(self.cl)
        
    
    def resize(self,e):
        # print(f"{e.data.split(',')}")
        data = e.data.split(',')
        print(data)
        self.cl.height = int(float(data[1])) - 150
        self.cl.width = int(float(data[0])) - 200
        self.update()
            
    
    
class hoge2(ft.UserControl):
    # def __init__(self) -> None:
    #     super().__init__(self)
    #     self.first_name = ft.Ref[ft.TextField]()
    #     self.greeting = ft.Ref[ft.Column]()
    
    def build(self):
        return ft.Container([
            ft.TextField(),
            ft.Column(),
            ft.IconButton(icon=ft.icons.PAUSE_CIRCLE,on_click=self.hogehoge()),
        ])
        
    def hogehoge(self):
        # self.greeting.current.controls.append(ft.Text(self.first_name.current.value))
        # self.page.update()
        self.update()

class hoge3:
    def __init__(self) -> None:
        pass
        
ft.app(main)