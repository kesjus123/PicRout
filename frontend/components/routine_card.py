import flet as ft

class RoutineCard(ft.Container):
    def __init__(self, title: str, time: str, is_completed: bool = False, on_complete=None):
        self.title_text = title
        self.time_text = time
        self.is_completed = is_completed
        self.on_complete = on_complete
        
        super().__init__(
            bgcolor=ft.Colors.WHITE,
            padding=14,
            border_radius=20,
            margin=ft.margin.only(bottom=10),
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12, offset=ft.Offset(0, 2)),
            content=self._build_content()
        )

    def _build_content(self):
        if self.is_completed:
            action_btn = ft.Container(
                content=ft.Icon(ft.Icons.CHECK, color=ft.Colors.WHITE, size=20),
                bgcolor="#22C55E",
                width=40,
                height=40,
                border_radius=20,
                alignment=ft.alignment.center,
            )
        else:
            action_btn = ft.ElevatedButton(
                text="Completar",
                bgcolor="#15803D",
                color=ft.Colors.WHITE,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                on_click=self.on_complete
            )

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=12,
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.Icons.BOOK_ROUNDED, color="#15803D", size=24),
                            bgcolor="#DCFCE7",
                            padding=10,
                            border_radius=12,
                        ),
                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text(self.title_text, weight=ft.FontWeight.BOLD, size=15, color="#1F2937"),
                                ft.Text(self.time_text, size=12, color="#9CA3AF"),
                            ]
                        )
                    ]
                ),
                action_btn
            ]
        )
