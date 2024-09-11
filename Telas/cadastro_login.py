import flet as ft

class CadastroScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def show(self):
        self.page.title = "Cadastro"
        self.page.controls.clear()  # Limpa a tela

        # Adiciona campos para o cadastro 
        username_field = ft.TextField(label="Usuário", hint_text="Digite seu usuário")
        email_field = ft.TextField(label="Email", hint_text="Digite seu email")
        password_field = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True)

        cadastro_button = ft.ElevatedButton(text="Cadastrar", on_click=self.on_register_click, bgcolor="#2196F3")  # Azul
        back_button = ft.ElevatedButton(text="Voltar", on_click=self.on_back_click, bgcolor="#FF5722")  # Vermelho

        # Adiciona os controles na página
        self.page.add(
            ft.Column(
                controls=[
                    username_field,
                    email_field,
                    password_field,
                    cadastro_button,
                    back_button
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        self.page.update()

    def on_register_click(self, e):
        # Lógica para registrar o usuário (não implementada aqui)
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Registro realizado com sucesso!"),
            bgcolor="#00ff00",
            open=True
        )
        self.page.update()

    def on_back_click(self, e):
        from home_screen import home_screen
        home_screen(self.page)  # Volta para a tela home

def login_screen(page: ft.Page):
    page.title = "Login"
    page.controls.clear()  # Limpa a tela

    # Adiciona campos para o login
    email_field = ft.TextField(label="Email", hint_text="Digite seu email")
    password_field = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True)

    def on_login_click(e):
        # Lógica para o login (não implementada aqui)
        page.snack_bar = ft.SnackBar(
            ft.Text("Login realizado com sucesso!"),
            bgcolor="#00ff00",
            open=True
        )
        page.update()

    login_button = ft.ElevatedButton(text="Login", on_click=on_login_click, bgcolor="#2196F3")  # Azul
    back_button = ft.ElevatedButton(text="Voltar", on_click=lambda e: home_screen(page), bgcolor="#FF5722")  # Vermelho

    # Adiciona os controles na página
    page.add(
        ft.Column(
            controls=[
                email_field,
                password_field,
                login_button,
                back_button
            ],
            alignment="center",
            horizontal_alignment="center"
        )
    )
    page.update()
