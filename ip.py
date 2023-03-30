try:
	import os, sys, time, random
	from bs4 import BeautifulSoup
	import threading, requests
except Exception as ex:
	print('Installing requests ...')
	os.system('requests')
	os.system('pip install bs4')

os.system('clear')
banner = '''                                          
.___                 .___        _____       
|   |_____           |   | _____/ ____\____  
|   \____ \   ____ |   |/    \   __\/  _ \ 
|   |  |_> > /___/ |   |   |  \  | (  <_> )
|___|   __/          |___|___|  /__|  \____/ 
    |__|                      \/             \n
Telegram: https://t.me/darkspacetermux'''

colors = ['', '', '']
print(banner)

def prnt(r):
	print('\n[Страна] : ' + r['country'])
	print('[Регион] : ' + r['region'])
	print('[Город] : ' + r['city'])
	print('[Местоположение] : ' + r['loc'])
	print('[Провайдер] : ' + r['org'])
	print('[Часовой пояс] : ' + r['timezone'])
	print('[Почтовый индекс] : ' + r['postal'])

def check_ip():
	os.system('clear')
	print(banner)
	ip = input('\nHапишите Ip >> ')
	res = requests.get('https://ipinfo.io/' + ip + '/json')
	r = res.json()
	prnt(r)

def my_ip():
	req = requests.get('https://www.iplocation.net/').text
	os.system('clear')
	print(banner)
	ip = '2'
	if ip:
	 	soup = BeautifulSoup(req, 'html.parser')
	 	response = soup.find_all('div', class_='row')

	 	tables = response[1].find('table', class_='iptable')
	 	tr = tables.find_all('tr')

	 	for t in tr:
	 		th = t.find('th')
	 		td = t.find('td')

	 		print('\n' + th.text + ' : ' + td.text)
	pass

def check_command(command):
	command = int(command)
	if command == 1:
		check_ip()
	if command == 2:
		my_ip()
	if command == 0:
		sys.exit()

menu = '''
[1] Ip пробив
[2] Cобственный Ip
[0] Выход
'''
def run():
	print(menu)
	command = input(colors[1] + '>>> ')
	if command.isdigit():
		check_command(command)
	else:
		print('error')
		sys.exit()	
run()
