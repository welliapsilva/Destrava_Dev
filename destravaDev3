import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import openpyxl
from openpyxl.utils import get_column_letter
from time import sleep
from datetime import datetime
import schedule

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver
link= 'https://produto.mercadolivre.com.br/MLB-4709516948-baixo-4-cordas-ativo-giannini-gb-200a-tbl-translucent-blue-_JM?searchVariation=182880038073#searchVariation%3D182880038073%26position%3D2%26search_layout%3Dgrid%26type%3Ditem%26tracking_id%3D8ef4e890-e491-4984-aca7-69b7efb0cb13'

def coletar_dados():
    driver = iniciar_driver()
    driver.get(link)
    driver.maximize_window()
    sleep(1.5)
    #clicar no CEASA escolhido
    valor = driver.find_element(By.XPATH,'//*[@id="price"]/div/div[1]/div[1]/span/span/span[2]')
    valorbaixo= valor.text
    sleep(2)
    driver.quit()

    # Criando arquivo
    wb = openpyxl.Workbook()
    ws = wb.active

    # Criando cabeçalho do arquivo
    header_row = ['Data', 'Hora', 'Produto', 'Preço','Link']
    for col, value in enumerate(header_row, start=1):
        ws.cell(row=1, column=col).value = value

    # Gerando a data 
    produto_nome = 'Baixo Giannini Standard GB-200A TBL 4 Cordas Azul Ativo'  # nome do produto
    preco = valorbaixo
    data_consulta = datetime.now().strftime('%Y-%m-%d')
    hora_consulta = datetime.now().strftime('%H:%M:%S')

    # cria nova coluna com os valores
    row_data = [data_consulta, hora_consulta, produto_nome, preco,link]
    for col, value in enumerate(row_data, start=1):
        ws.cell(row=2, column=col).value = value

    # calva o arquivo
    wb.save('Pesquisa de preços.xlsx')
    print("Cotação realizada com sucesso! Será retomada em 30 minutos.")
    
coletar_dados()

schedule.every(30).minutes.do(coletar_dados)

while True:
    schedule.run_pending()
    sleep(1)
