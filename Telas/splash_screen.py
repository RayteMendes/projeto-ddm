import flet as ft
import asyncio
from home_screen import home_screen

async def splash_screen(page: ft.Page, image_path=None):
    page.title = "Tela Splash"
    page.bgcolor = "#00193b"  # Define o fundo como branco

    # Centraliza a imagem, se um caminho foi fornecido
    if image_path:
        logo = ft.Image(src=image_path, width=500, height=500)
    else:
        logo = ft.Image(src="assets/minha_imagem.png", width=500, height=500)  # Placeholder padrão

    text = ft.Text("Carregando...",style=ft.TextThemeStyle.DISPLAY_SMALL,color="blue",font_family="Agrandir")
    progress_bar = ft.ProgressBar(width=200)

    # Adiciona os controles (imagem, barra de progresso, texto) na tela splash
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    logo,
                    progress_bar,
                    text
                ],
                alignment="center",
                horizontal_alignment="center"
            ),
            alignment=ft.alignment.center,
            expand=True  # Expande para preencher a tela inteira
        )
    )
    page.update()

    # Simula o carregamento com uma barra de progresso
    for i in range(101):  
        progress_bar.value = i / 100
        page.update()
        await asyncio.sleep(0.02)  # Espera não bloqueante

    # Após a splash screen, carrega a tela home
    from home_screen import home_screen
    home_screen(page)
