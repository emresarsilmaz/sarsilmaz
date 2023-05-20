import requests, httplib, urllib
import socket
from platform import system
import os
import sys, time
import re
import threading
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL
sb  =   Style.BRIGHT

user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"
cookie = {
	"ZHE" : "e575478f2d96c337f146e56958ae0e47",
	"PHPSESSID" : "hv5ua3dfstmd8uprhvqs7bpbn0"
	}


def zonehh():
	print("""
	    |---| Grabb Sites From Zone-h |--|
		\033[91m[1] \033[95mGrabb Sites By Notifier
		\033[91m[2] \033[95mGrabb Sites By Onhold
		""")
	sec = int(raw_input("Choose : "))
	if sec == 1:
		notf = raw_input("\033[95mEnter notifier: \033[92m")

		for i in range(1, 51):
			dz = requests.get(url + notf +"/page=" + str(i), cookies=cookie)
			dzz = dz.content
			print(url + notf +"/page=" + str(i))
			if '<html><body>-<script type="text/javascript"' in dzz:
				print("Please Enter Cookie")
				sys.exit()
			elif '<input type="text" name="captcha" value=""><input type="submit">' in dzz:
				print("Please Solve Captcha In Zone-H website")
				sys.exit()
			else:
				Hunt_urls = re.findall('<td>(.*)\n							</td>', dzz)
				if '/mirror/id/' in dzz:
					for xx in Hunt_urls:
						qqq = xx.replace('...','')
						print '    ['  + '*' + '] ' + qqq.split('/')[0]
						with open(notf + '.txt', 'a') as rr:
							rr.write("http://" + qqq.split('/')[0] + '\n')
				else:
					print("Grabbing Sites is finished ^_^")
					sys.exit()

	elif sec == 2:
		print(":* __Grabb Sites By Onhold__ ^_^")
		for qwd in range(1, 51):
			rb = requests.get(urll + "/page=" + str(qwd) , cookies=cookie)
			dzq = rb.content

			if '<html><body>-<script type="text/javascript"' in dzq:
				print("Please Solve Captcha In Zone-H website")
				sys.exit()

			elif "captcha" in dzq:
				print("Please Solve Captcha In Zone-H website")
			else:
				Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
				for xxx in Hunt_urlss:
					qqqq = xxx.replace('...','')
					print '    ['  + '*' + '] ' + qqqq.split('/')[0]
					with open('onhold_zone.txt', 'a') as rrr:
						rrr.write("http://" + qqqq.split('/')[0] + '\n')
	else:
		print("Oh Shit")

def ip():
 x = open(raw_input('List Sites:'),'r').readlines()
 for sites in x:
     sites = sites.rstrip()
     try:
         ips = socket.gethostbyname(sites)
         print Fore.RED+sites+Fore.CYAN+' => '+Fore.GREEN+ips
         xx = open('IP.txt','a').write(ips+'\n')
     except:
         pass


def clearscrn():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def helper4():
	clearscrn()
	banner = """\033[33m\033[91m\033[93m
	==========================================================
	=======================Rootinabox==========================
			Telegram : @rootinabox	  		 
		Channel : https://t.me/Rootinabox_Channel
	==========================================================
"""
	print("""\033[91m
	==========================================================
	=======================Rootinabox==========================
			Telegram : @rootinabox	  		 
		Channel : https://t.me/Rootinabox_Channel
	==========================================================
    [+]1. Zone-H Grabber
    [+]2. IPs Grabber from list of sites
			""")
	try:
		qq = int(raw_input("\033[91m[-] \033[90mroot@Charlotte~#\033[95m : \033[90m"))
		if qq == 1:
			clearscrn()
			print(banner)
			zonehh()
		if qq == 2:
			clearscrn()
			print(banner)
			ip()
			

	except:
		pass
helper4()