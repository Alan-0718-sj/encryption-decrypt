import os
import time
from cryptography.fernet import Fernet
from tkinter import Tk, filedialog
import win32api
from dotenv import load_dotenv, dotenv_values
from pyfiglet import Figlet
import getpass

# Carregando nome do usuário
username = win32api.GetUserName()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def print_com_animacao(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def animacao_aguarde(tempo_total, texto="Aguarde...", intervalo=0.5):
    start_time = time.time()
    while time.time() - start_time < tempo_total:
        print(texto, end='', flush=True)
        time.sleep(intervalo)
        print('\r' + ' ' * len(texto) + '\r', end='', flush=True)
        time.sleep(intervalo)

def escolher_pasta():
    root = Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title="Escolha a pasta com os arquivos")
    return pasta

# Verifica se o conteúdo está criptografado
def esta_criptografado(conteudo):
    return conteudo.startswith(b'ENCRYPTED:')

# Remove o marcador de criptografia
def remover_marcador(conteudo):
    return conteudo[len(b'ENCRYPTED:'):]

# Pede ao usuário para escolher a pasta
pasta_escolhida = escolher_pasta()

if not pasta_escolhida:
    print_com_animacao(" NENHUMA PASTA FOI ESCOLHIDA... ENCERRANDO O PROGRAMA ".upper().center(70, '🔴'))
    exit()

todos_arquivos = []

# Percorre os arquivos na pasta escolhida
for file in os.listdir(pasta_escolhida):
    if file in ["malware.py", "key.key", "decr.py"]:
        continue
    caminho_completo = os.path.join(pasta_escolhida, file)
    if os.path.isfile(caminho_completo):
        todos_arquivos.append(caminho_completo)

# Exibe todos os arquivos encontrados, um por linha
limpar_tela()
preview_text = Figlet(font='slant')
print(preview_text.renderText('DECRYPT'))
print("Arquivos encontrados:")
for arquivo in todos_arquivos:
    print(arquivo, sep='\n')

# Carrega a chave de criptografia
try:
    with open(os.path.join(pasta_escolhida, "key.key"), "rb") as chave_arquivo:
        chave = chave_arquivo.read()
except FileNotFoundError:
    print_com_animacao(" CHAVE DE CRIPTOGRAFIA NÃO ENCONTRADA! ENCERRANDO O PROGRAMA ".upper().center(70, '⚫'))
    exit()

# Carrega as configurações do arquivo .env
config = {**dotenv_values(".env.shared"), **dotenv_values(".env.secret")}
pass_key = config.get("MY_KEY_ACESS", "default_key")
passphrase = pass_key

# Solicita a senha ao usuário
userpass = getpass.getpass("\nDigite a senha que você recebeu de nós: ")
name = 'Verboten'
if userpass == passphrase:
    for file in todos_arquivos:
        try:
            with open(file, "rb") as arquivo:
                conteudo = arquivo.read()
            if esta_criptografado(conteudo):
                conteudo_sem_marcador = remover_marcador(conteudo)
                conteudo_decriptado = Fernet(chave).decrypt(conteudo_sem_marcador)
                with open(file, "wb") as arquivo:
                    arquivo.write(conteudo_decriptado)
            else:
                print(f"O arquivo {file} não está criptografado.")
        except Exception as e:
            print(f"Erro ao decriptar o arquivo {file}: {e}")
    animacao_aguarde(tempo_total=3)
    print_com_animacao(f" OLÁ USUÁRIO: {username} VOCÊ RECUPEROU SEUS ARQUIVOS. ".upper().center(70, '🟢') + "\n")
else:
    animacao_aguarde(tempo_total=5)
    print_com_animacao(" SENHA INCORRETA! ABRA UM CHAMADO... ".upper().center(70, '⚫') + "\n")
