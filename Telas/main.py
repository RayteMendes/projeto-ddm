import flet as ft
import asyncio
from splash_screen import splash_screen

def main(page: ft.Page):
    image_path = "Telas\IMG\Memória.gif"  # Caminho para a imagem local
    asyncio.run(splash_screen(page, image_path=image_path))

# Inicia o aplicativo
ft.app(target=main)
