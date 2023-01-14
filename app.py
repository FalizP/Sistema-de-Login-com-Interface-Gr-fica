import PySimpleGUI as sg

PATH = 'dados.txt'

sg.theme('DarkAmber')
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('Login'), sg.Button("Criar")],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('login', layout=layout)


def main():
    while True:
        event, values = window.read()
        if event == 'Login':
            fazerLogin(values)
        if event == "Criar":
            criarUsuario(values)
        if event == sg.WIN_CLOSED:
            break


def fazerLogin(values):
    if values['usuario'] == values['senha']:
        window['mensagem'].update('A senha e o usuário devem ser diferentes')
        return

    userValido = isUsuarioValido(values)
    if userValido:
        window['mensagem'].update('Login Concluido!')
    else:
        window['mensagem'].update('Usuário ou senha incorretos!')


def isUsuarioValido(values):
    dados = []
    try:
        with open(PATH, 'r', encoding='utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                dados.append(linha.split())

                for dado in dados:
                    nome = dado[0]
                    password = dado[1]
                if values['usuario'] == nome and values['senha'] == password:
                    return True

    except:
        return


def criarUsuario(values):
    try:
        with open(PATH, 'a', encoding="utf-8", newline='') as arquivo:
            arquivo.write(str(f'{values["usuario"]} {values["senha"]}\n'))
    except:
        window['mensagem'].update("Erro ao criar novo usuário!")
    finally:
        window['mensagem'].update('Usuário cadastrado com sucesso!')


if __name__ == '__main__':
    main()
