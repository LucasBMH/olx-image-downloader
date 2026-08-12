from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
from time import time
import requests

#------------------vars----------------#

headers = {"User-Agent": "Mozilla/5.0"}

img_url_list = []

opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--headless=new")           #Executa o Chrome em modo headless (sem interface gráfica)
opcoes.add_argument("--window-size=1366,768")
opcoes.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36")

#-----------------code--------------------#

print("""
\033[35m

 $$$$$$\  $$\       $$\   $$\ 
$$  __$$\ $$ |      $$ |  $$ |
$$ /  $$ |$$ |      \$$\ $$  |
$$ |  $$ |$$ |       \$$$$  / 
$$ |  $$ |$$ |       $$  $$<  
$$ |  $$ |$$ |      $$  /\$$\ 
 $$$$$$  |$$$$$$$$\ $$ /  $$ |
 \______/ \________|\__|  \__|
      
      Images Downloader

\033[m""")


while True:
    pagina = str(input("\033[32mInsira a URL da página: \033[m"))
    pagina = pagina.strip()

    if not pagina:
        print("URL INVÁLIDA, insira novamente ")
        print("")

    else:
        break

print('')
print("\033[33mAguarde...\033[m")


#abre o navegador 
navegador = webdriver.Chrome(options=opcoes)

#acessa o site
navegador.get(pagina)

#coloca o navegador em tela cheia 
navegador.maximize_window()

# Define um tempo de espera até conseguir clicar no elemento
espera = WebDriverWait(navegador, 10) 

#Isso aqui é para fechar um POP-UP caso tenha
body = navegador.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.ESCAPE) #aperta ESC para fechar o pop-up

#------------------------------------

#localizar a foto do carro e clica para expandir as outras fotos
foto_expandir = espera.until(ec.presence_of_element_located((By.XPATH, '//*[@id="item-gallery-image-0"]//img'))) 
navegador.execute_script("arguments[0].scrollIntoView(true);", foto_expandir)
navegador.execute_script("arguments[0].click();", foto_expandir)


#encontra todas as tags IMG no código fonte
imgs = navegador.find_elements(By.TAG_NAME, "img")


#pega o atributo SRC (link da foto) de cada tag IMG encontrada
#filtra para pegar somente as imagens nescessárias 
#armazena elas na lista 

for img in imgs:
    if 'images' in img.get_attribute("src") and 'img.olx.com.br' in img.get_attribute("src") and 'jpg' not in img.get_attribute("src"):
        img_url_list.append(img.get_attribute("src"))

#fecha o navegador
navegador.quit()


#cria a pasta para salvar as imagens 
#mkdir cria a pasta, exist_ok=True evita erro se a pasta já existir

output_folder = Path.home() / "Downloads" / "OLX_Images"
output_folder.mkdir(parents=True, exist_ok=True)


#para cada imagem na lista de links, faz o download da imagem e levante uma exeção se houver erro
for url in img_url_list:
    try:
        pega_imagem = requests.get(url, headers=headers, timeout=10)
        pega_imagem.raise_for_status() 

                
        #caminho completo do arquivo de saída
        #esta linha nomeia o arquivo com base no nome original do arquivo na URL, é basicamente um tratamento de string
        imagem_baixada = Path(urlparse(url).path).name

        #caso a imagem não tenha nome, define um nome padrão, pegando o tempo atual em milissegundos como base 
        if not imagem_baixada:
            imagem_baixada = f"imagem_olx_{int(time.time() * 1000)}"

        
        with open(output_folder / imagem_baixada, "wb") as f: #abre a pasta de saída, e escreve a imagem no arquivo. Vai ser feito isso para cara URL dentro da lista
            f.write(pega_imagem.content)

        print("\033[32mImagem baixada com Sucesso! \033[m")

    except requests.exceptions.RequestException as erro:
        print(f"\033[31mErro ao baixar a imagem. {erro}\033[m")

input("Presione Enter para finalizar...")

