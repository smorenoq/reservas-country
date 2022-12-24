import requests


request_data = {
    'Login1$Username': '023341',
    'Login1$Password': '023341342'
}
requests.post('https://amigo.countryclub.com.co/Socios/wfLogin.aspx?ReturnUrl=%2fSocios%2f', data=request_data)