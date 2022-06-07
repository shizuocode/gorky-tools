import requests
import urllib.parse
from bs4 import BeautifulSoup
import threading

# headers file
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'referer': 'https://www.google.com/',
		'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'Connection' : 'keep-alive',
		'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
}
# Google dorks clas
class Gdorks:
	def __init__(self, query):
		self.query = urllib.parse.quote_plus(query)
	
	# Search In Google
	def search(self):
		# Parsing cookies from cookies.txt
		rcookies = open("cookies.txt", "r").read().split(";")
		cookies = {}
		for i in rcookies:
			k, v = i.strip().split("=")
			cookies[k.strip()] = v.strip()
		req = requests.session()
		target = f"https://www.google.com/search?q={self.query}&source=hp&oq={self.query}&sclient=gws-wiz"
		req = requests.get(target, allow_redirects=True, cookies=cookies, headers=headers)
		self.grab(str(req.text))
		listnextpage = self.nextpage(str(req.text))
		threadlist = []
		for i in listnextpage:
			t = threading.Thread(target=self.searchpage, args=(i,))
			threadlist.append(t)
		for t in threadlist:
			t.start()
		for t in threadlist:
			t.join()
		req.cookies.clear()
	# Search next page in Google
	def searchpage(self, pagepath):
		req = requests.get("https://www.google.com"+pagepath, allow_redirects=True, cookies=cookies, headers=headers)
		self.grab(str(req.text))

	# Grabbing site result form page
	def grab(self, content):
		fi = BeautifulSoup(content, "html.parser")
		lista = fi.find_all("a", href=True)
		if len(lista)<3:
			print("[Error!] -- Try to rewrite your cookies in cookies.txt!")
		else:
			for i in lista:
				if "http" in i["href"] and "google" not in i["href"]:
					print(i["href"])
					with open("result.txt", "a") as fwrite:
						fwrite.write(str(i["href"]) + "\n")
	
	# Grabbing Url for Next Page
	def nextpage(self, content):
		fi = BeautifulSoup(content, "html.parser")
		lista = fi.find_all("a", href=True)
		listpage = []
		for i in lista:
			if "&start=" in i["href"]:
				listpage.append(i["href"])
		listpage = list(set(listpage))
		return listpage

# Banner
def banner():
	print("|----------------------------------|")
	print("""
░██████╗░░█████╗░██████╗░██╗░░██╗██╗░░░██╗
██╔════╝░██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝
██║░░██╗░██║░░██║██████╔╝█████═╝░░╚████╔╝░
██║░░╚██╗██║░░██║██╔══██╗██╔═██╗░░░╚██╔╝░░
╚██████╔╝╚█████╔╝██║░░██║██║░╚██╗░░░██║░░░
░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░""")
	print("|----------------------------------|")
	print("Gorky is simple tools for grabbing website list in google search.")
	print("Source : https://github.com/shizuocode/gorky-tools")
	print("......")
	print("......")
# main program	
def main():
	banner()
	test = input("Input Dork List Filename : ")
	try:
		with open(test, "r", encoding="utf-8") as dorklist:
			dorklists = dorklist.read().split("\n")
			for i in dorklists:
				Gdorks(i).search()
	except:
		print("Please input valid google dork lists")
if __name__ == '__main__':
	main()
