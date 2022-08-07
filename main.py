from 	bs4 						import BeautifulSoup
from 	colorama 					import Fore
from 	requests_futures.sessions 	import FuturesSession
import 	concurrent.futures
import os
import pystyle
from pystyle import Colors, Colorate, Center
session = FuturesSession(max_workers=250)


logo = """
██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██╔██╗ ██║██║   ██║██║   ██║   █████╗      ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝"""


def printLogo():
    print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logo, 1)))

os.system(f"title Discordservers Scraper - Ready!")
global count
count = 0
printLogo()
print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   discordservers.com", 1)))
kw = str(input('\n[+] Enter your keyword to scrape: '))
def writeline(filename,data):
	with open(filename,'a') as f:
		f.write('\n' + data)
		f.close()
def scrape():
	invites = []
	def scrp(session,amount,skip):
		url = f'https://search.discordservers.com/?term=&size={amount}&from={skip}&keyword='+kw
		servers = session.get(url).result().json()['results']
		for server in servers:
			global count
			invite = server['customInvite']
			if invite != None and len(invite) > 0 and invite not in invites:
				print(Fore.YELLOW +"["+ Fore.CYAN + "+" + Fore.YELLOW + "] " + Fore.RESET + f"https://discord.gg/{invite}")
				invites.append(invite)
				writeline('invites.txt',invite)
				count += 1
				os.system(f"title Discordservers Scraper - Scraped {count} servers.")
	with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
		skip = 0
		skip_interval = 50
		futures = []
		amount = 50
		while True:
			futures.append(executor.submit(scrp,session,amount,skip))
			skip += skip_interval
amount = input("Press " + Fore.MAGENTA + "enter " + Fore.RESET+ "to start.")
scrape()