import flet as ft

def home_screen(page: ft.Page):
    page.title = "Tela Home"
    page.controls.clear()  # Limpa a tela

    def show_cadastro_screen(e):
        from cadastro_login import CadastroScreen
        CadastroScreen(page).show()

    def show_login_screen(e):
        from cadastro_login import login_screen
        login_screen(page)

    # Container estilizado
    options_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(text="Cadastrar", on_click=show_cadastro_screen, bgcolor="#2196F3"),  # Azul
                ft.ElevatedButton(text="Login", on_click=show_login_screen, bgcolor="#2196F3")  # Azul
            ],
            alignment="center",
            horizontal_alignment="center"
        ),
        alignment=ft.alignment.center,
        padding=20,
        bgcolor=ft.colors.WHITE,  # Fundo da caixa
        border=ft.border.all(2, color="#000000"),  # Borda preta
        border_radius=10,  # Cantos arredondados
        width=300,  # Largura fixa para a caixa
        height=200,  # Altura fixa para a caixa
        margin=20  # Margem externa
    )

    # Adiciona a caixa estilizada na página
    page.add(
        ft.Container(
            content=options_container,
            alignment=ft.alignment.center,
            expand=True  # Expande para preencher a tela inteira
        )
    )
    page.update()
