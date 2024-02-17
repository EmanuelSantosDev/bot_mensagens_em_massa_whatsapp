import pyautogui
import webbrowser
from time import sleep


telefones = []


# Adicionando contatos à lista de telefones
with open('contatos.txt', 'r') as lista_contatos:
    for contato in lista_contatos:
        # retirando o caractere de nova linha
        telefones.append(contato.split('\n')[0])


for telefone in telefones:
    # Abrindo o navegador
    webbrowser.open(f'https://wa.me/{telefone}')
    sleep(10)
    # Clicando no botão que autoriza a abertura do Aplicativo do WhatsApp
    pyautogui.click(777, 244, duration=1)
    sleep(10)
    # Ativando o campo de texto
    pyautogui.click(603, 690, duration=2)
    # Escrevendo e enviando a mensagem
    pyautogui.typewrite('Teste Bot Envio WhatsApp', interval=0.1)
    pyautogui.press('enter')
    sleep(5)
    # Fechando o navegador para evitar o travamento do browser
    # (evitar múltiplas abas abertas)
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    # Pausa de 300 segundos à fim de evitar o bloqueio do bot
    sleep(300)
