# É onde fica o código para a interface gráfica
# Tudo que existir de visual vai ficar aqui
# É principalmente aqui que usaremos o PySimpleGUI
import PySimpleGUI as sg 

# Windows => Janela
# Layout => O que vai mostrar na janela
#        => Lista de listas
#           Cada sublista é uma "linha" da janela
#           Cada elemento é um componente visual

lista = ['Administradores', 'Alunos']
def get_layout():
    layout = [
        [
            sg.Text('Eu sou um texto'),
            sg.In(),
            sg.FileBrowse('Selecione o seu código', file_types = (('Arquivos Python', '*.py')
            ,)
            ),
            ],
            [
                sg.Text('Selecione a lista de destinatário'),
                sg.Combo(lista, default_value = lista[1]),
            ],
            [
                sg.Text('Insira o título: '),
                sg.In(key = '-Title-')
            ],
            [
                sg.Text('Insira o conteúdo do e-mail: '),
                sg.MLine(key = '-Content-'),
            ],
            [
                sg.Button('Enviar', key = '-Send-'),
                sg.Button('Gerenciar Listas', key = '-ListEditor-')
            ],
    ]

    return layout

def get_window():
    return sg.Window("Teste de janela", get_layout())