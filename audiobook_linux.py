import pyttsx3
import pdfplumber

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Configurando a voz para uma mais natural
voices = engine.getProperty('voices')
# Substitua o índice pelo ID da voz que você escolheu
engine.setProperty('voice', voices[0].id)

# Ajustar a taxa de fala (quanto menor, mais lenta e clara a voz)
engine.setProperty('rate', 190)  # Ajuste este valor conforme necessário (padrão é 200)

# Ajustar o volume da fala (entre 0.0 e 1.0)
engine.setProperty('volume', 1.0)

# Lendo arquivo PDF
pdf = pdfplumber.open("Historia do Linux.pdf")

# Gerando lista de páginas do livro, exceto as páginas 1 a 8
paginas = pdf.pages[8:25]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

# Ajustando o texto para melhor qualidade de leitura
texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

# Salvando o texto em um arquivo de áudio
engine.save_to_file(texto_final, "audiobook.mp3")
engine.runAndWait()
