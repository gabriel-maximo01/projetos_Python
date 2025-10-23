import os
from tkinter.filedialog import askdirectory
# essa biblioteca é usada para abrir uma janela de diálogo para selecionar diretórios

#NOTA MENTAL!!!!!!! NO PYTHON O TAB É MUITO IMPORTANTE, ELE DEFINE BLOCOS DE CÓDIGO TIPO OQUE TÁ DENTRO DOQUE, IGUAL O {} DO JAVA

caminho = askdirectory(title="seleciona a pasta vey")
# abre uma janela para o usuário selecionar um diretório com o texto que eu mandei

lista_de_arquivos = os.listdir(caminho)
# lista todos os arquivos e pastas no diretório selecionado é tipo o "cd"

locais ={
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".tiff"],
    "documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "musicas": [".mp3", ".wav", ".aac", ".flac"],
    "videos": [".mp4", ".avi", ".mkv", ".mov"],
    "compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "fontes": [".ttf", ".otf", ".fon"],

}
# 'locais' serve para selecionar onde fica cada tipo de arquivo, não para mover ou criar a pasta ainda

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}{arquivo}")
    # separa o nome do arquivo da sua extensão

    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
    #basicamente ele vai olhar as pastas ou "caminhos" e ver se tem a as "pastas" que eu criei lá emcima, e se não tiver ele cria
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
                #esses (f"") são para formatar strings, ou seja, colocar variáveis dentro de strings