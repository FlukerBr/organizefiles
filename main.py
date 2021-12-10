import os
import PySimpleGUI as sg
def organizar(path):
    listfile = os.listdir(path)
    for file in listfile:
        if '.' in file:
            print(file)
            i = file.find('.') + 1
            ii = file.find('.')
            nomepasta = file[i:]
            with open(r'{0}/{1}'.format(path, file), 'rb') as fr:
                filerb = fr.read()
            try:
                os.makedirs(f'{path}/{nomepasta}')
            except FileExistsError:
                pass
            with open(r'{0}/{1}/{2}'.format(path, nomepasta, file), 'wb') as fw:
                fw.write(filerb)
            os.remove(r'{0}/{1}'.format(path, file))
def tela():
    sg.theme('Default1')
    layout = [
        [sg.Text('Caminho : ', text_color='gray'), sg.Input(key='path', size=(23, 1)), sg.FolderBrowse(button_text='Escolher...', button_color=('white', '#008080'), key='pasta', )],
        [sg.Button('Organizar', pad=(120, 0), button_color=('white', '#008080'))],
        [sg.Text('Created by FlukerBr', size=(30, 1), key='text', text_color='#008080')]
    ]
    window = sg.Window('Organizador de Arquivos', layout, size=(325, 110), icon='assets/icon.ico')
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'navegar':
            path = value['path']
            window['path'].update(path)
        if event == 'Organizar':
            organizar(value['path'])
tela()
# os.chdir(path)