from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600','--incognito' ]
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://www.climatempo.com.br/')
sleep(2)

localizacao= pyautogui.locateCenterOnScreen('permitir.png') #encontrar o botao pemitir
sleep(1)
pyautogui.click(localizacao[0],localizacao[1])#clica para aceitar a localizaçao
sleep(5)


temperatura_element = driver.find_element(By.ID, "current-weather-temperature")
temperatura = temperatura_element.text
condicao= driver.find_element(By.ID, "current-weather-condition")
condTemp= condicao.text

if temperatura:  # verifica se o valor de temperature não é vazio
    print(f'A temperatura hoje esta:{temperatura}, e o tempo esta: {condTemp}')
else:
    print("não encontrata")


sleep(10)
driver.quit()