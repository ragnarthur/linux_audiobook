# Audiobook do Livro "História do Linux"

Este projeto cria um audiobook do livro "História do Linux" a partir de um arquivo PDF utilizando a biblioteca `gTTS` em Python.

## Sumário

- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Script](#script)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O objetivo deste projeto é automatizar a criação de um audiobook a partir de um livro em formato PDF. Utilizando Python, extraímos o texto do PDF e o convertemos em áudio, que é então salvo como um arquivo MP3.

## Requisitos

Antes de executar o script, certifique-se de ter o seguinte:

- Python 3.x instalado
- Bibliotecas Python:
  - `gtts`
  - `pdfplumber`

## Instalação

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/audiobook-historia-linux.git
    cd audiobook-historia-linux
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # No Windows: env\Scripts\activate
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque o arquivo PDF do livro "História do Linux" no diretório do projeto com o nome `Historia do Linux.pdf`.

2. Execute o script `audiobook.py`:

    ```bash
    python audiobook.py
    ```

   O script irá:
   - Ler as páginas do livro, exceto as páginas 1 a 8.
   - Extrair o texto das páginas especificadas.
   - Converter o texto em áudio.
   - Salvar o áudio como `audiobook_completo.mp3`.

## Script

```python
from gtts import gTTS
import pdfplumber

# Lendo arquivo PDF
pdf = pdfplumber.open("Historia do Linux.pdf")

# Gerando lista de páginas do livro, exceto as páginas 1 a 8
paginas = pdf.pages[8:30]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

# Ajustando o texto para melhor qualidade de leitura
texto_final = texto_livro.replace('\n', ' ').replace('.', '. ').replace(',', ', ')

# Convertendo texto para fala usando gTTS
tts = gTTS(text=texto_final, lang='pt-br')
tts.save("audiobook_completo.mp3")

print("Audiobook completo gerado com sucesso!")
 ```