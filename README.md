# OLX Images Downloader

Automação desenvolvida em Python para facilitar o download de imagens
de anúncios de veículos.

## 📌 Sobre o projeto

Este projeto foi desenvolvido para solucionar uma necessidade operacional
de uma empresa do setor automotivo.

O usuário informa a URL de um anúncio e a aplicação utiliza Selenium
para acessar a página, localizar as imagens disponíveis e obter suas URLs.

Após a coleta, as imagens são baixadas utilizando Requests e armazenadas
automaticamente em uma pasta no computador do usuário.

## ⚙️ Funcionamento

1. Usuário informa a URL do anúncio
2. Selenium abre a página em modo headless
3. A aplicação localiza as imagens do anúncio
4. As URLs são coletadas
5. Requests realiza o download das imagens
6. Os arquivos são salvos em `Downloads/OLX_Images`

## 🛠️ Tecnologias

- Python
- Selenium
- Requests
- Pathlib
- Chrome WebDriver

## 🚀 Como executar

...

## 📁 Estrutura simples

1 arquivo python

## ⚠️ Observação

Este projeto foi desenvolvido para fins de automação de uma tarefa
operacional e deve ser utilizado respeitando os termos de uso e as
políticas aplicáveis ao site acessado.

É possivel converter para um .exe para uso no windows sem a nescessidade de ter o python instalado
