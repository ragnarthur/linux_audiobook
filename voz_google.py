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
