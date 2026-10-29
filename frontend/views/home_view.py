import flet as ft
from frontend.components.routine_card import RoutineCard

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/home",
            padding=0,
            bgcolor="#F8FAF8"
        )
        self.page = page

        # Lista de rutinas de prueba
        routines = [
            RoutineCard("Estudiar", "4:00 PM", is_completed=False),
            RoutineCard("Hacer ejercicio", "6:00 PM", is_completed=False),
            RoutineCard("Meditar", "8:00 PM", is_completed=True),
        ]

        # Contenido de la vista
        self.controls = [
            ft.Column(
                expand=True,
                justify_content=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(
                        padding=ft.padding.symmetric(horizontal=20, vertical=10),
                        content=ft.Column(
                            controls=[
                                ft.Text("Rutinas de hoy", weight=ft.FontWeight.BOLD, size=18, color="#111827"),
                                *routines
                            ]
                        )
                    ),
                    self._build_bottom_nav()
                ]
            )
        ]

    def _build_bottom_nav(self):
        return ft.Container(
            height=70,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.only(top_left=24, top_right=24),
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.IconButton(icon=ft.Icons.HOME, icon_color="#15803D"),
                    ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, icon_color="#9CA3AF"),
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        bgcolor="#22C55E",
                        content_color=ft.Colors.WHITE,
                        shape=ft.CircleBorder(),
                        on_click=lambda e: print("Abrir cámara para verificar con IA")
                    ),
                    ft.IconButton(icon=ft.Icons.STAR_BORDER, icon_color="#9CA3AF"),
                    ft.IconButton(icon=ft.Icons.PERSON_OUTLINE, icon_color="#9CA3AF"),
                ]
            )
        )
