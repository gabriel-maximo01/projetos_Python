# 📄 Explicando o Código de Organizar Arquivos

Esse código em Python serve para **organizar os arquivos de uma pasta** em subpastas de acordo com o tipo do arquivo.  
Por exemplo, imagens vão pra pasta `imagens`, PDFs pra `documentos`, músicas pra `musicas` e assim por diante.  

Tudo de forma automática 😎

---

## 🧰 Bibliotecas que usamos

```python
import os
from tkinter.filedialog import askdirectory
```

- `os` → serve pra mexer com arquivos e pastas (listar, criar, mover, etc).  
- `tkinter.filedialog.askdirectory` → abre uma **janela para você escolher uma pasta** no computador.  

---

## 🛠 Selecionando a pasta que queremos organizar

```python
caminho = askdirectory(title="seleciona a pasta vey")
```

- Isso abre uma janela para o usuário selecionar a pasta.  
- O caminho da pasta escolhida fica guardado na variável `caminho`.

---

## 📂 Listando todos os arquivos da pasta

```python
lista_de_arquivos = os.listdir(caminho)
```

- `os.listdir(caminho)` pega **todos os arquivos e pastas que estão dentro da pasta escolhida**.  
- Isso retorna uma lista com os nomes dos arquivos.

---

## 📌 Criando a tabela de tipos de arquivos

```python
locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".tiff"],
    "documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "musicas": [".mp3", ".wav", ".aac", ".flac"],
    "videos": [".mp4", ".avi", ".mkv", ".mov"],
    "compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "fontes": [".ttf", ".otf", ".fon"],
}
```

- Aqui a gente diz **quais tipos de arquivos vão pra qual pasta**.  
- `locais` é tipo um “mapa” que liga cada extensão a uma pasta.

---

## 🔄 Passando por cada arquivo da pasta

```python
for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}{arquivo}")
```

- `for arquivo in lista_de_arquivos:` → pega um arquivo de cada vez da lista.  
- `os.path.splitext(...)` → separa o **nome do arquivo** da **extensão**.  
- Exemplo: `foto.jpg` → `nome = foto`, `extensao = .jpg`

---

## 📂 Verificando e criando as pastas

```python
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
```

- Pra cada arquivo, o código olha **em qual categoria ele se encaixa**.  
- Se a pasta correspondente **não existir ainda**, ela é criada automaticamente com `os.mkdir()`.  

**Visualmente:**
```
Arquivo: foto.jpg
→ Categoria: imagens
→ Pasta 'imagens' existe? ❌ → cria pasta
```

---

## ➕ Movendo o arquivo pra pasta certa

```python
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
```

- `os.rename()` serve pra **mover o arquivo de lugar**.  
- Ele pega o arquivo original e coloca dentro da pasta correspondente.

**Visualizando o fluxo:**
```
📁 Pasta original
   foto.jpg   → move para → 📁 imagens/foto.jpg
   documento.pdf → move para → 📁 documentos/documento.pdf
   musica.mp3 → move para → 📁 musicas/musica.mp3
```

---

## ⚡ Resumo do funcionamento

1. Abre uma janela para escolher a pasta.  
2. Lista todos os arquivos dentro da pasta escolhida.  
3. Define quais tipos de arquivos vão pra quais pastas.  
4. Para cada arquivo:
   - Descobre a extensão do arquivo  
   - Verifica em qual categoria ele se encaixa  
   - Cria a pasta se não existir  
   - Move o arquivo para a pasta correspondente  

---

💡 **Dica de iniciante:**

- O **tab é muito importante no Python**! Ele define blocos de código, igual `{}` no Java.  
- Se errar a indentação, o código **não vai funcionar**.  
- Teste com poucos arquivos primeiro, pra ver se a organização está funcionando direitinho.
