#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService 
import time

unames = ['023341', '023340']
pwords = ['023341342', '023340682']
turnos = [12, 13]
num_canchas = [1,2,3,4]
fecha = '12/10/2023'

for uname, pword, turno in zip(unames, pwords, turnos):
    for num_cancha in num_canchas:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("disable-infobars"); # disabling infobars
            chrome_options.add_argument("--disable-extensions"); # disabling extensions
            chrome_options.add_argument("--disable-gpu"); # applicable to windows os only
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--incognito')
            driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
            

            driver.get(r'https://amigo.countryclub.com.co/Socios/wfLogin.aspx?ReturnUrl=%2fSocios%2fDefault.aspx')

            # Find the username/email field and send the username to the input field.
            username = driver.find_element("id", "Login1_UserName") 
            username.send_keys(uname)

            # Find the password input field and send the password to the input field.
            password = driver.find_element("id", "Login1_Password") 
            password.send_keys(pword)

            # Click sign in button to login the website.
            driver.find_element("id", "Login1_LoginButton").click()

            driver.get(f'http://amigo.countryclub.com.co/Socios/Deportes/wfConsultas.aspx?DeporteID=1&Fecha={fecha}')

            button_turno = driver.find_element("id", f"ctl00_ContentPlaceHolder1_btnTurno{turno}")
            button_turno.click()
 
            time.sleep(2)

            button_cancha = driver.find_element("id", f"ctl00_ContentPlaceHolder1_dlCanchas_ctl0{num_cancha-1}_btnReservar")
            button_cancha.click()

            time.sleep(2)
            driver.close()
            break

        except Exception as e:
            print(e)