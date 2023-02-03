#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

uname = '023340'
pword = '023340682'

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("disable-infobars"); # disabling infobars
    chrome_options.add_argument("--disable-extensions"); # disabling extensions
    chrome_options.add_argument("--disable-gpu"); # applicable to windows os only
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=chrome_options)

    driver.get('https://amigo.countryclub.com.co/Socios/wfLogin.aspx?ReturnUrl=%2fSocios%2f')

    # Find the username/email field and send the username to the input field.
    username = driver.find_element("id", "Login1_UserName") 
    username.send_keys(uname)

    # Find the password input field and send the password to the input field.
    password = driver.find_element("id", "Login1_Password") 
    password.send_keys(pword)

    # Click sign in button to login the website.
    driver.find_element("id", "Login1_LoginButton").click()

    button_reservas = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnReservasDeportivas")
    button_reservas.click()

    button_turno = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnTurno10")
    button_turno.click()

    time.sleep(3)

    button_turno = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnDiaSiguiente")
    button_turno.click()

    time.sleep(3)

    button_turno = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnTurno10")
    button_turno.click()

    time.sleep(2)

    button_turno = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnDiaSiguiente")
    button_turno.click()

    time.sleep(2)

    button_turno = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnTurno10")
    button_turno.click()

    time.sleep(2)

    num_cancha = 1
    button_cancha = driver.find_element("id", f"ctl00_ContentPlaceHolder1_dlCanchas_ctl0{num_cancha-1}_btnReservar")
    button_cancha.click()

except Exception as e:
    with open('logs.txt', 'w') as f:
        f.write(str(e))
