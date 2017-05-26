#/usr/bin/python3
# -*- coding:utf-8 -*-
try:
	from twilio.rest import TwilioRestClient
except:
	print('')
	print('pip install twilio')
	print('easy install twilio')
	exit()
import os
import time
#
os.system('clear')
ACCOUNT_SID = ""
AUTH_TOKEN = ""
from_ = ""
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

global end, verde, azul, amarelo, vermelho, purpleClaro, normal, cyanClaro,
end = '\033[0m'
#Palheta de Cores
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'



BannerOld = """
____________¶¶¶
___________¶___¶
____________¶¶¶
____________¶_¶
____________¶_¶
__________¶¶¶_¶¶¶                  
________¶¶__¶¶¶__¶¶¶            ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀█  ▒█▀▀▀ █░░ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█  
______¶¶__¶¶¶¶¶¶¶___¶           ░▀▀▀▄▄ ▒█▒█▒█ ░▀▀▀▄▄  ▒█▀▀▀ █░░ █░░█ █░░█ █░░█ █▀▀ █▄▄▀ 
_____¶_______________¶          ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄█  ▒█░░░ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ 
____¶_________________¶
____¶_________________¶              +==========================================+
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶            |      SMS Sending Spam and Flooder        |
____¶____¶_______________¶           +==========================================+
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶           | ♚ Coded: łuŧЋ1єr ルシアー                |
____¶___¶___¶___________¶¶¶          | ♚ Contact: @Xcultevil (Telegram)         |
____¶___¶___¶_¶¶¶___¶¶¶__¶¶          | ♚ Date: 07/03/2017                       |
____¶___¶___¶_¶¶¶___¶¶¶__¶¶          | ♚ I take no responsibilities for the     |
____¶___¶___¶___________¶¶¶          |   use of this program !                  |
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶           +==========================================+
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶             |          łαbørαŧøriø Fαηŧαsмα            |
____¶_________________¶              +==========================================+
____¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶__¶__¶__¶__¶                          [1] ✉ Mensagem Normal
____¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶                          [2] ✉ Spam
____¶__¶___¶__¶__¶__¶                          [3] ✉ Historico de Mensagens
____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶_________________¶¶¶

"""

BannerEnd = """_____________¶____¶ 
_________¶_¶¶¶¶¶¶¶¶¶¶ 
_____¶¶¶¶¶¶¶_________¶ 
___¶¶¶¶¶_____________¶ 
___¶_________________¶ 
____¶________________¶¶ 
____¶¶________________¶ 
_____¶________________¶¶ 
_____¶¶_______¶¶¶____¶¶¶ 
______¶_____¶¶___¶¶_¶___¶ 
______¶_____¶¶_____¶____¶ 
______¶¶____¶______¶¶¶¶¶¶¶     ╭━━━┳━╮╭━┳━━━╮╭━━━┳╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
_______¶____¶¶__¶¶¶_____¶¶     ┃╭━╮┃┃╰╯┃┃╭━╮┃┃╭━━┫┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱┃╭━━╯╱╱╱╱┃┃
______¶¶¶¶____¶¶¶¶_____¶¶      ┃╰━━┫╭╮╭╮┃╰━━╮┃╰━━┫┃╭━━┳━━┳━╯┣━━┳━╮┃╰━━┳━╮╭━╯┃
______¶¶¶_______________¶¶     ╰━━╮┃┃┃┃┃┣━━╮┃┃╭━━┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯┃╭━━┫╭╮┫╭╮┃
_______¶¶¶______________¶¶     ┃╰━╯┃┃┃┃┃┃╰━╯┃┃┃╱╱┃╰┫╰╯┃╰╯┃╰╯┃┃━┫┃╱┃╰━━┫┃┃┃╰╯┃
________¶_____¶¶¶¶¶¶¶¶¶¶¶      ╰━━━┻╯╰╯╰┻━━━╯╰╯╱╱╰━┻━━┻━━┻━━┻━━┻╯╱╰━━━┻╯╰┻━━╯
_______¶¶_______¶¶¶¶¶ 
______¶¶¶¶¶_____¶ 
___¶¶¶¶__¶¶¶¶¶¶¶¶ 
__¶¶____¶¶_____¶¶ 
_¶¶_____¶¶______¶¶ 
¶¶______¶¶_______¶¶ 
_¶¶¶¶¶___¶¶______¶¶ 
_¶__¶¶¶¶¶¶_______¶¶ 
¶¶____¶___________¶¶ 
¶____¶¶__________¶¶¶ 
¶____¶¶____________¶ 
¶_____¶___________¶¶¶ 
¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶ 
¶______¶_________¶___¶ 
¶¶¶¶__¶__________¶_¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶____¶ 
___¶¶___¶__¶____¶ 
___¶____¶__¶____¶ 
___¶¶___¶__¶____¶¶ 
__¶_______¶¶¶¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶"""


print azul + BannerOld

try:
	opt = raw_input(amarelo + '[*] Choose an Option > ')
except KeyboardInterrupt:
	print(vermelho+"\n \n[-] Exiting....")
	time.sleep(3)
	print cyanClaro + BannerEnd
	exit()
print('')

def Ma1n():
	global body, to, from_ 
	body = raw_input(cyanClaro + "[*] Digite sua Mensagem > ")
	print('')
	to =   raw_input(cyanClaro + '[*] Digite numero do alvo > ')
	print('')
	from_ = ""
	img =  raw_input(amarelo + "[*] Deseja enviar uma imagem? [y/N] > ")
	if img == 'y':
		img2 = raw_input(amarelo + '[*] Deseja enviar mais de uma (1) imagens? [y/N] > ')
		print('')
		if img2 == 'n':
			SendImage()
		elif img2 == 'y':
			MultipleImages()
	elif img == 'n':
		SendMessage()
	else:
		print('')
		print(vermelho + '[-] Wrong option...\n')
		main()
	return body, to, from_


def SendMessage():
	message = client.messages.create(
	    body = body, 	
    	to = to,
    	from_ = from_,
	)
	print('')
	print(verde +'✉ SMS - Flooder ✉')
	print('')
	print (vermelho + '[*] ID > '+azul+message.sid+end)
	print('')

def SendImage():
	media_url = raw_input("[*] Digite a url da sua imagem > ")
	message = client.messages.create(	
   		body = body, 
   		to = to,
  	 	from_ = from_,
 	 	media_url = media_url,
	)
	print('')
	print ('[+] '+verde+'✉'+vermelho+' Imagem  Enviada Com Sucesso!' + end)
	print('')

def MultipleImages():
	numbers = raw_input(amarelo + '[*] Digite o numero de imagens [2/3] > ')
	print('')
	if numbers == '2':
		media_url1 = raw_input(amarelo + '[*] Digite a url da sua primeira imagem > ')
		media_url2 = raw_input(amarelo + '[*] Digite a url da sua segunda imagem > ')
		print('')
		message = client.messages.create(
			body = body,   # Message body, if any
	    	to = to,	
    		from_ = from_,
    		media_url=[
       		 	media_url1,
        		media_url2,
    		],
		)
		print('')
		print(verde+'✉'+vermelho+'Imagens Enviadas Com Sucesso!...')
		print('')
	elif numbers == '3':
		media_url1 = input('[1] Digite a url da sua Primeira imagem > ')
		media_url2 = input('[2] Digite a url da sua Segunda imagem > ')
		media_url3 = input('[3] Digite a url da sua Terceira imagem > ')
		print('')
		message = client.messages.create(
			body = body,  # Message body, if any
    		to=to,
    		from_=from_,
    		media_url=[
   		   		media_url1,
   		     	media_url2,
        		media_url3,
    		],
		)
		print('')
		print(verde+'[+]'+vermelho+'Imagens Enviadas Com Sucesso!...')		
	else:
		print('')
		print(vermelho + "Digite uma opção valida...")
		print('')

def Retrieving():
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	for message in client.messages.list():
		Historico = (message.body)
		print ("Historico de mensagens Enviadas > ", Historico )


def SPAM():
	global body, to, from_
	print(vermelho + "+==========================================+")
	print(vermelho + "|              ✉ SPAM MODE ✉               |")
	print(vermelho + "+==========================================+")
	print('')
	body = raw_input(cyanClaro + "[*] Digite sua Mensagem > ")
	print('')
	wordlist =   raw_input(cyanClaro + '[*] Digite Sua Lista de Numeros > ')
	print('')
	to = open(wordlist, 'r').readlines()
	from_ = "+19402023964 "
	FloodNumber = int(input(verde + "Digite o numero de Flooder > "))
	print('')
	img =  raw_input(amarelo + "[*] Deseja enviar uma imagem? [y/N] > ")
	print('')
	if img == 'y':
		img2 = raw_input(amarelo + '[*] Deseja enviar mais de uma (1) imagens? [y/N] > ')
		print('')
		if img2 == 'n':
			for i in rage(1, FloodNumber+1):
				SendImage()
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')
		elif img2 == 'y':
			for i in rage(1, FloodNumber+1):
				MultipleImages()
				print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
				print('')

	for i in range(1, FloodNumber+1):
		SendMessage()
		print purpleClaro + "\r ✉ SMS - Flooder ✉ - Total enviados > %i" % i
		print('')


def main():
	if opt == '1':
		try:
			Ma1n()
		except KeyboardInterrupt:
			print(vermelho + '\n \n[-] Exiting...')
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
			exit()
	elif opt == '3':
		try:
			Retrieving()		
		except KeyboardInterrupt:
			print(vermelho + "\n \n[-] Exiting....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
	elif opt == '2':
		try:
			SPAM()
		except KeyboardInterrupt:
			print(vermelho+"\n \n[-] Exiting....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(vermelho+'\n\n[-] Exiting...')
		time.sleep(3)
		os.system('clear')
		print cyanClaro + BannerEnd
		exit()
