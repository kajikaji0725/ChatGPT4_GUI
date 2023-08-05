from chatgpt4_gui import View, Setting
import flet as ft


def main(page: ft.Page):

    view = View(page)
    page.add(view)
    setting = Setting(view)
    page.on_resize = view.resize
    pick_files_dialog = ft.FilePicker(on_result=view.save_file_result)
    page.overlay.append(pick_files_dialog)

    appBar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("ChatGPT for GUI"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.DELETE, on_click=view.open_dialog),
            ft.IconButton(ft.icons.DOWNLOAD,
                          on_click=pick_files_dialog.save_file),
            ft.IconButton(
                ft.icons.HOME, on_click=lambda _: page.go('/home')),
            ft.IconButton(ft.icons.SETTINGS,
                          on_click=lambda _: page.go('/setting')),
        ],
    )

    page.appbar = appBar
    page.update()
    page.window_min_width = 740

    def route_change(route):
        if page.route == "/home":
            page.views.append(
                ft.View(
                    "/home",
                    [
                        view,
                        appBar
                    ],
                )
            )

        if page.route == "/setting":
            page.views.append(
                ft.View(
                    "/setting",
                    [
                        setting,
                        appBar
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        if len(page.views) > 1:
            page.update()
        else:
            page.go('/')

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
