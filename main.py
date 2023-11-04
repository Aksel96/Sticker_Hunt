import time

import flet as ft

# Colores usados en los efectos
WHITECOLOR = str(ft.colors.WHITE)
BLACKCOLOR = str(ft.colors.SURFACE_VARIANT)
TEMPCOLOR = str(ft.colors.RED)

imagenes = []  # Arreglo temporal de imagenes


# Funcion para cambiar el color del fondo cuando entra el mouse en las imagenes
def on_hover(e):
    e.control.bgcolor = WHITECOLOR if e.data == "true" else BLACKCOLOR
    e.control.update()


def on_click_image(e):  # Respuesta al evento de clic en las imagenes

    # Animacion de click
    e.control.bgcolor = TEMPCOLOR
    e.control.update()
    time.sleep(0.1)
    e.control.bgcolor = WHITECOLOR
    e.control.update()

    # Añadimos al arreglo de favoritos la direccion de la imagen
    imagenes.append(e.control.content.src)

    # Alert dialog de favorito
    dlg_modal = dlg = ft.AlertDialog(
        title=ft.Text("¡Guardado!"), content=ft.Text("Se agrego correctamente a favoritos"),
        on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(j):
        j.page.dialog = dlg_modal
        dlg.open = True
        j.page.update()

    open_dlg(e)
    print(imagenes)


def add_image(i, images):  # Agrega las imagenes a un contenedor
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


def main(page: ft.Page):
    # Widget del app bar (Barra de arriba)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Sticker Hunt"),
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

    # Widget del rail de la izquierda
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Crear"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Favoritos"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HISTORY_TOGGLE_OFF),
                selected_icon_content=ft.Icon(ft.icons.HISTORY_TOGGLE_OFF_SHARP),
                label="Historial",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Ajustes"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    # Creamos un gridView donde se mostraran las imagenes
    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    # Ciclo for para añadir las imagenes en el GridView
    for i in range(0, 20):
        add_image(i, images)
        page.update()

    # Agregamos las imagenes en una columna, en otra un divisor y ultima el rail
    page.add(
        ft.Row(
            [
                ft.Column([images], alignment=ft.MainAxisAlignment.START, expand=True),
                ft.VerticalDivider(width=1),
                rail,
            ],
            expand=True,
        )
    )


ft.app(target=main)

# Agregar en settings, con un popmenuButton ,  modo claro y about (creditos)
