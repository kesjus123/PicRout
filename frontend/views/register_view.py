import flet as ft

class RegisterView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/register",
            bgcolor="#F8FAF8",
            padding=20
        )
        self.page = page

        self.controls = [
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text("Crear cuenta", size=24, weight=ft.FontWeight.BOLD, color="#15803D"),
                    ft.TextField(label="Nombre completo", border_radius=12),
                    ft.TextField(label="Correo electrónico", border_radius=12),
                    ft.TextField(label="Contraseña", password=True, can_reveal_password=True, border_radius=12),
                    ft.ElevatedButton(
                        text="Crear cuenta gratis",
                        bgcolor="#15803D",
                        color=ft.Colors.WHITE,
                        width=300,
                        height=48,
                        on_click=lambda e: page.go("/home") # Navega al Home
                    )
                ]
            )
        ]
