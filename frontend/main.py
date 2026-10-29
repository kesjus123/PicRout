import flet as ft
from frontend.views.home_view import HomeView
from frontend.views.register_view import RegisterView

def main(page: ft.Page):
    page.title = "PicRout"
    page.window.width = 380
    page.window.height = 750

    def route_change(route):
        page.views.clear()
        
        # Enrutador simple
        if page.route == "/register":
            page.views.append(RegisterView(page))
        elif page.route == "/home":
            page.views.append(HomeView(page))
        else:
            # Ruta por defecto al iniciar
            page.views.append(RegisterView(page))
            
        page.update()

    page.on_route_change = route_change
    page.go("/register") # Arranca en el registro

ft.app(target=main)
