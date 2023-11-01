import time

import flet as ft

WHITECOLOR = str(ft.colors.WHITE)
BLACKCOLOR = str(ft.colors.SURFACE_VARIANT)
TEMPCOLOR = str(ft.colors.RED)


# Funcion para cambiar el color del fondo cuando entra el mouse en las imagenes
def on_hover(e):
    e.control.bgcolor = WHITECOLOR if e.data == "true" else BLACKCOLOR
    e.control.update()


def on_click_image(e):  # Funcion cuando le das click a las imagenes
    # Animacion de click
    e.control.bgcolor = TEMPCOLOR
    e.control.update()
    time.sleep(0.1)
    e.control.bgcolor = WHITECOLOR
    e.control.update()


def main(page: ft.Page):
    # Widget del app bar (Barra de arriba)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Hunt stickers"),
        automatically_imply_leading=True,
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.TextField(label="Buscar sticker:", hint_text="Ingresa tu busqueda:", content_padding=10, ),
            ft.FloatingActionButton(
                content=ft.Row(
                    [ft.Icon(ft.icons.SEARCH), ft.Text("Buscar")],
                    spacing=10,
                ),
                bgcolor=ft.colors.SURFACE_VARIANT,
                shape=ft.RoundedRectangleBorder(radius=10),
                width=100,
                mini=True,
            )
        ],
    )
    # Widget de mostrar las imagenes
    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(images)

    for i in range(0, 50):
        images.controls.append(
            ft.Container(
                content=
                ft.Image(
                    src=f"https://picsum.photos/150/150?{i}",
                    fit=ft.ImageFit.NONE,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                ),
                margin=5,
                padding=5,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.SURFACE_VARIANT,
                on_hover=on_hover,
                on_click=on_click_image,
            )
        )
    page.update()


# LLamada a la aplicacion de flet
ft.app(target=main)
