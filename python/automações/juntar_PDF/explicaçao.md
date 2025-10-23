# 📄 Explicando o Código de Juntar PDFs (Visual e Fácil)

Esse código em Python junta vários PDFs que estão numa pasta e transforma tudo em **um único PDF**.  
Aqui vai o passo a passo de forma **visual e divertida** 😎

---

## 🧰 Bibliotecas que usamos

```python
import PyPDF2  # pra mexer com PDFs
import os      # pra mexer com arquivos e pastas
```

---

## 🛠 Criando o objeto que vai juntar os PDFs

```python
mesclar = PyPDF2.PdfMerger()
```

- `mesclar` é como uma **caixinha** onde vamos colocar todos os PDFs que queremos juntar.

---

## 📂 Listando os arquivos da pasta

```python
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)
```

- Primeiro, pegamos **todos os arquivos da pasta `arquivos`**  
- Depois, colocamos em **ordem alfabética** para não bagunçar a ordem dos PDFs  
- Por fim, mostramos a lista no console ✅  

**Visualizando a lista:**
```
📁 arquivos/
   ├─ 01_intro.pdf
   ├─ 02_capitulo.pdf
   └─ 03_final.pdf
```

---

## 🔄 Passando por cada arquivo

```python
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        mesclar.append(f"arquivos/{arquivo}")
```

### 🔹 Como funciona na prática

1. `for arquivo in lista_arquivos:` → pega um arquivo de cada vez  
2. `if ".pdf" in arquivo:` → verifica se é PDF  
3. `mesclar.append(...)` → adiciona dentro da **caixinha `mesclar`**

**Visualmente:**

```
📂 arquivos/
   01_intro.pdf   ---> 📦 mesclar
   02_capitulo.pdf ---> 📦 mesclar
   03_final.pdf   ---> 📦 mesclar
```

---

## 📝 Criando o PDF final

```python
mesclar.write("PDF Final.pdf")
```

- Agora pegamos **tudo que está na caixinha `mesclar`** e salvamos em um único arquivo:

```
📦 mesclar ---> PDF Final.pdf
```

- Resultado: todos os PDFs da pasta `arquivos` viram **um só arquivo chamado `PDF Final.pdf`** 🎉

---

## ⚡ Resumindo o fluxo (passo a passo visual)

```
[ pasta 'arquivos' ]
01_intro.pdf
02_capitulo.pdf
03_final.pdf
       |
       v
[ adiciona ao objeto 'mesclar' ]
       |
       v
[ salva tudo junto ]
       |
       v
📄 PDF Final.pdf
```

---

💡 **Dicas rápidas pra iniciantes:**

- A pasta `arquivos` **precisa existir** e ter PDFs dentro.  
- Se quiser testar, coloque alguns PDFs pequenos na pasta antes.  
- O programa ignora arquivos que **não terminam em `.pdf`**.  

---

