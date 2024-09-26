# Ferramenta de Criptografia e Descriptografia de Arquivos

Este projeto contém dois scripts Python que utilizam criptografia para proteger ou recuperar arquivos em uma pasta específica. Ambos os códigos foram desenvolvidos com o objetivo de criptografar e descriptografar arquivos usando a biblioteca `cryptography.fernet`, além de oferecer uma interface gráfica simples para a escolha de diretórios.

## Funcionalidades

### 1. **Código de Criptografia de Arquivos**

Este código permite criptografar arquivos em uma pasta escolhida pelo usuário. Ele ignora certos arquivos críticos como scripts de malware ou chaves já existentes e aplica criptografia em todos os demais arquivos.

#### Funcionalidades:
- Gera uma **chave de criptografia** única para os arquivos.
- Adiciona um marcador indicando que o arquivo foi criptografado.
- Exibe uma animação enquanto criptografa os arquivos.
- Salva a chave de criptografia em um arquivo chamado `key.key` na mesma pasta dos arquivos.
- Exibe uma mensagem personalizada ao final do processo, indicando o nome do usuário e o status da criptografia.

#### Como utilizar:
1. Execute o script.
2. Escolha a pasta onde estão localizados os arquivos que deseja criptografar.
3. Os arquivos criptografados serão marcados e protegidos.
4. A chave de criptografia será gerada e salva no arquivo `key.key` dentro da pasta escolhida.

### 2. **Código de Descriptografia de Arquivos**

Este código descriptografa arquivos que foram previamente criptografados pelo script de criptografia. Ele solicita uma senha ao usuário, que deve corresponder à senha armazenada em um arquivo `.env`, e então descriptografa os arquivos da pasta selecionada.

#### Funcionalidades:
- Carrega a **chave de criptografia** previamente gerada.
- Remove o marcador de criptografia dos arquivos.
- Solicita uma senha ao usuário e valida com a senha armazenada no arquivo `.env`.
- Exibe uma mensagem de sucesso ou falha ao descriptografar os arquivos.
- Ignora arquivos que não estão criptografados ou que foram configurados para serem ignorados.

#### Como utilizar:
1. Execute o script.
2. Escolha a pasta com os arquivos que deseja descriptografar.
3. Insira a senha recebida anteriormente (armazenada em um arquivo `.env`).
4. Se a senha estiver correta, os arquivos serão descriptografados e recuperados.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `cryptography`
  - `tkinter`
  - `win32api`
  - `pyfiglet`
  - `dotenv`
  - `getpass`

## Instalação

1. Clone o repositório.
2. Instale as dependências necessárias usando o `pip`:
   ```bash
   pip install cryptography pyfiglet python-dotenv
