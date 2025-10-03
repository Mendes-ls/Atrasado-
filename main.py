from flet import *

def main(page: Page):

    alerta = AlertDialog(
        modal=True, 
        title=Text('atenção'), 
        content=Text('Esta é uma mensagem de alerta.')
    )
    

    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.overlay.append(alerta)
        page.update()
    page.add(
        Text('Olá, Mundo!'),
        ElevatedButton("Mostrar Alerta", on_click=abrir_alerta)
    )
app(target=main)