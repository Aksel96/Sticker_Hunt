import time
import flet as ft

# Colores usados en los efectos
HOVER_COLOR_HOME = str(ft.colors.WHITE)
HOVER_COLOR_FAV = str(ft.colors.RED)
BLACKCOLOR = str(ft.colors.SURFACE_VARIANT)
TEMPCOLOR = str(ft.colors.WHITE)
BG_COLOR_APPBAR = str(ft.colors.SURFACE_VARIANT)
BG_COLOR_IMAGES = str(ft.colors.SURFACE_VARIANT)

# Tiempo para borrar de la papelera
TIEMPODELETE = 5

imagenes = []  # Arreglo temporal de imagenes
papeleraList = []


def on_hover(e):  # Funcion para cambiar el color del fondo cuando entra el mouse en las imagenes

    e.control.bgcolor = HOVER_COLOR_HOME if e.data == "true" else BLACKCOLOR
    e.control.update()


def on_hover_fav(e):
    e.control.bgcolor = HOVER_COLOR_FAV if e.data == "true" else BLACKCOLOR
    e.control.update()


def on_hover_papelera(e):
    e.control.bgcolor = HOVER_COLOR_FAV if e.data == "true" else BLACKCOLOR
    e.control.update()


def on_click_image(e):  # Respuesta al evento de clic en las imagenes

    # Animacion de click
    e.control.bgcolor = TEMPCOLOR
    e.control.update()
    time.sleep(0.1)
    e.control.bgcolor = HOVER_COLOR_HOME
    e.control.update()

    # Guardamos la direccion de la imagen
    source_image = str(e.control.content.src)

    def close_dlg(e):
        dlg_modal.open = False
        e.page.update()

    def yes_option_fav(e):
        imagenes.append(source_image)
        print("Se agrego")
        close_dlg(e)

    def no_option_fav(e):
        print("No se agrego")
        close_dlg(e)

    # Alert dialog de favorito
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("¡Confirmacion!"),
        content=ft.Text("¿Quieres agregar esta imagen a favoritos?"),
        actions=[
            ft.TextButton("Si", on_click=yes_option_fav),
            ft.TextButton("No", on_click=no_option_fav),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=no_option_fav,
    )

    def open_dlg(j):
        j.page.dialog = dlg_modal
        dlg_modal.open = True
        j.page.update()

    open_dlg(e)


def on_click_image_favorites(e):  # Respuesta al evento de clic en las imagenes

    # Animacion de click
    e.control.bgcolor = TEMPCOLOR
    e.control.update()
    time.sleep(0.1)
    e.control.bgcolor = HOVER_COLOR_FAV
    e.control.update()

    # Guardamos la url de la imagnen
    elemento = str(e.control.content.src)

    def close_dlg(e):
        dlg_modal.open = False
        e.page.update()

    def yes_option_fav(e):
        papeleraList.append(elemento)
        imagenes.remove(elemento)
        print("Se elimino de fav")
        close_dlg(e)

    def no_option_fav(e):
        print("No se quito")
        close_dlg(e)

    # Alert dialog de papelera
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("¡AVISO!"),
        content=ft.Text("¿Quieres mandar a la papelera este elemento?"),
        actions=[
            ft.TextButton("Si", on_click=yes_option_fav),
            ft.TextButton("No", on_click=no_option_fav),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=no_option_fav,
    )

    def open_dlg(j):
        j.page.dialog = dlg_modal
        dlg_modal.open = True
        j.page.update()

    open_dlg(e)


def on_click_image_papelera(e):  # Respuesta al evento de clic en las imagenes

    # Animacion de click
    e.control.bgcolor = TEMPCOLOR
    e.control.update()
    time.sleep(0.1)
    e.control.bgcolor = HOVER_COLOR_FAV
    e.control.update()

    # Guardamos la url de la imagnen
    elemento = str(e.control.content.src)

    def close_dlg(e):
        dlg_modal.open = False
        e.page.update()

    def yes_option_fav(e):
        papeleraList.remove(elemento)
        print("Se elimino permanentemente")
        close_dlg(e)

    def no_option_fav(e):
        print("No se quito")
        close_dlg(e)

    # Alert dialog de eliminacion
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("¡IMPORTANTE!"),
        content=ft.Text("¿Quieres eliminar definitivamente este elemento?"),
        actions=[
            ft.TextButton("Si", on_click=yes_option_fav),
            ft.TextButton("No", on_click=no_option_fav),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=no_option_fav,
    )

    def open_dlg(j):
        j.page.dialog = dlg_modal
        dlg_modal.open = True
        j.page.update()

    open_dlg(e)


def rail_widget(page):  # Widget del rail de la izquierda

    rail = ft.NavigationRail(
        selected_index=None,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.HOME, text="Inicio", on_click=lambda _: page.go("/")),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.IconButton(icon=ft.icons.FAVORITE_BORDER,
                                           on_click=lambda _: page.go("/favorite")),
                label="Favoritos",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.IconButton(icon=ft.icons.RESTORE_FROM_TRASH,
                                           on_click=lambda _: page.go("/papelera")),
                label="Papelera",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED,
                                           on_click=lambda _: page.go("/ajustes")),
                label="Ajustes",
            ),
        ],
        on_change=None,
    )
    return rail


def app_bar_widget():  # Widget del app bar (Barra de arriba)

    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Sticker Hunt"),
        automatically_imply_leading=True,
        center_title=False,
        bgcolor=BG_COLOR_APPBAR,
    )
    return appbar


def images_widget():  # Creamos un gridView donde se mostraran las imagenes

    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    return images


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
            bgcolor=BG_COLOR_IMAGES,
            on_hover=on_hover,
            on_click=on_click_image,
        )
    )


def add_image_favorites(i, favorites):
    favorites.controls.append(
        ft.Container(
            content=
            ft.Image(
                src=f"{imagenes[i]}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            ),
            margin=5,
            padding=5,
            alignment=ft.alignment.center,
            bgcolor=BG_COLOR_IMAGES,
            on_hover=on_hover_fav,
            on_click=on_click_image_favorites,
        )
    )


def add_image_papelera(i, papelera):
    papelera.controls.append(
        ft.Container(
            content=
            ft.Image(
                src=f"{papeleraList[i]}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            ),
            margin=5,
            padding=5,
            alignment=ft.alignment.center,
            bgcolor=BG_COLOR_IMAGES,
            on_hover=on_hover_papelera,
            on_click=on_click_image_papelera,
        )

    )


def main(page: ft.Page):
    def theme_changed(e):  # Elegir el tema de la aplicacion
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Tema claro" if page.theme_mode == ft.ThemeMode.LIGHT else "Tema oscuro"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.DARK
    c = ft.Switch(label="Tema oscuro", on_change=theme_changed)

    def route_change(route):  # Funcion para administrar el cambio de views
        page.views.clear()
        images = images_widget()
        favoritos = images_widget()
        papelera = images_widget()

        for i in range(0, 50):
            add_image(i, images)
            page.update()

        if imagenes:
            for i in range(len(imagenes)):
                add_image_favorites(i, favoritos)
                page.update()

        if papeleraList:
            for i in range(len(papeleraList)):
                add_image_papelera(i, papelera)
                page.update()

        page.views.append(
            ft.View(
                "/",  # View del inicio
                [
                    app_bar_widget(),
                    ft.Row(
                        [
                            ft.Column([images], alignment=ft.MainAxisAlignment.START, expand=True),
                            ft.VerticalDivider(width=1),
                            rail_widget(page),
                        ],
                        expand=True,
                    ), ], ))
        if page.route == "/favorite":  # View de los favoritos
            page.views.append(
                ft.View(
                    "/favorite",
                    [
                        app_bar_widget(),
                        ft.Row(
                            [
                                ft.Column([favoritos], alignment=ft.MainAxisAlignment.START, expand=True),
                                ft.VerticalDivider(width=1),
                                rail_widget(page),
                            ],
                            expand=True,
                        ), ], ))
        if page.route == "/papelera":  # View de la papelera
            page.views.append(
                ft.View(
                    "/papelera",
                    [
                        app_bar_widget(),
                        ft.Row(
                            [
                                ft.Column([papelera], alignment=ft.MainAxisAlignment.START, expand=True),
                                ft.VerticalDivider(width=1),
                                rail_widget(page),
                            ],
                            expand=True,
                        ), ], ))
        if page.route == "/ajustes":  # View de los ajustes
            page.views.append(
                ft.View(
                    "/ajustes",
                    [
                        app_bar_widget(),
                        ft.Row(
                            [
                                ft.Column([c, ft.Text("Copyright 2023")],
                                          alignment=ft.MainAxisAlignment.START, expand=True),
                                ft.VerticalDivider(width=1),
                                rail_widget(page),
                            ],
                            expand=True,
                        ), ], ))
        page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
