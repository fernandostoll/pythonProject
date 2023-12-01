import requests

site = 'https://api2023.galerax9x10.repl.co/05-08-2004'
signo = requests.get(site).json()

print(signo)