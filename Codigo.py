# Automação Web e Busca de Informações com Python

Para isso, vamos criar uma automação web:

- Usaremos o selenium
- Importante: baixar o webdriver

#######################################################################################################






from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui                    
from pyautogui import moveTo, click
import time 
from tkinter import messagebox 
# para rodar o chrome em 2º plano
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True 
from selenium import webdriver 
navegador = webdriver.Chrome(options=chrome_options)

# ação 
id_email =  "teste@gmail.com"
id_senha = "teste"
id_contato = "kalilinuxajuda@gmail.com"
tx_contato = "oi tudo bem to aqui pra lembra que a sua fatura de carta ed credito vencenceu"
id_texto =  "Testando o bot"
gmail  = "https://accounts.google.com/v3/signin/identifier?dsh=S-217845356%3A1665203374169767&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWpczCgohaNurxAMqaQHIGCKbWm6pHxsJ3U6SzoAFESTbnpN9xQ6hUp5X0b2LvV5F4O7r9R0"
#abri o navegador
pyautogui.alert(" Automação vai começar  !!! ")
navegador = webdriver.Chrome()   
navegador.get(gmail)
navegador.fullscreen_window() 

# Botando o  email 
navegador.find_element(By.XPATH,' //*[@id="identifierId"]').send_keys(id_email)
# clicando no botao de entrar  
navegador.find_element(By.XPATH,' //*[@id="identifierNext"]/div/button').send_keys(Keys.ENTER)
# Botando a senha  

time.sleep(9)
pyautogui.press('enter')
pyautogui.pause  = 2.8
pyautogui.write(id_senha)
time.sleep(3)
#clicar em entrar
navegador.find_element(By.XPATH,' //*[@id="passwordNext"]/div/button').send_keys(Keys.ENTER)
# clica no botao escrever carta 
time.sleep(9)
pyautogui.click(x=388, y=147)
time.sleep(9)

time.sleep(5)

time.sleep(1)
procurar =  "sim"

 
imag = pyautogui.locateCenterOnScreen('ok1.png', confidence=0.9)
pyautogui.click(imag.x, imag.y)
time.sleep(1)


time.sleep(9)
pyautogui.press('enter')
pyautogui.pause  = 2.8
# botao o de contato
pyautogui.write(id_email)

# botao o assunto 
time.sleep(5)
pyautogui.press('tab')
time.sleep(3)
pyautogui.press('tab')
pyautogui.write(id_texto)
time.sleep(5)
# Seu texto pra seu contato
navegador.find_element(By.XPATH,' /html/body/div[25]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div').send_keys(tx_contato)
# clica no botao ebviar 
#
navegador.find_element(By.XPATH,' /html/body/div[25]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1] ').send_keys(Keys.ENTER)
time.sleep(7)
navegador.close()


messagebox.showinfo('Automoção Email Gmail', \
      'Email enviado com susseso ')
