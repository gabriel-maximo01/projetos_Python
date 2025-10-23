import PyPDF2
import os

mesclar = PyPDF2.PdfMerger()
# cria um objeto PdfMerger para juntar arquivos PDF

lista_arquivos = os.listdir("arquivos")
# listdir serve para listar os arquivos de uma pasta
lista_arquivos.sort()
#sort() serve para ordenar a lista em ordem alfabética
print(lista_arquivos)
#print(lista_arquivos) mostra a lista de arquivos no console

for arquivo in lista_arquivos:
# esse for diz que pra cada arquivo na lista de arquivos:
    if ".pdf" in arquivo:
#se o arquivo for um pdf, ele será adicionado ao mesclar
        mesclar.append(f"arquivos/{arquivo}")
# append adiciona o arquivo ao objeto mesclar
mesclar.write("PDF Final.pdf")