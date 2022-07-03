from ast import While
import random
import PySimpleGUI as sg
from soupsieve import select

class DecidaPorMim():
    def __init__(self) -> None:
        self.resposta = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso NÃO!',
            'Acho que está na hora certa!',
            'Não, ainda tem tempo para pensar!',
            'Isso não é ideia boy',
            'AMAZIINNNN, claro que sim!!'
        ]

    def Iniciar(self):

        # Layout
        layout = [
            [sg.Text('Pergunta')],
            [sg.Input()],
            [sg.Output(size=(45, 10))],
            [sg.Button('Decida por mim')]
        ]
        # Janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True: 
            # Valores
            self.eventos, self.valores = self.janela.Read()
            # Acão
            if self.eventos == 'Decida por mim':
                print(random.choice(self.resposta))
                

decida = DecidaPorMim()
decida.Iniciar(

)
