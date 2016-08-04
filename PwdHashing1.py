	#Security Project
'''
		#Dictionaries Notes
#allow us to asssociate data.
inventory = {
			"bananas": [19]
			"apples": [20]
			}
print(inventory ["apples"])

has_key(key)
Test for the presence of key in the dictionary. has_key() is deprecated in favor of key in d.

'''


import hashlib
from hashlib import *
import time

logins = {		#DICTIONARY OF USERNAMES AND PASSWORDS
		"username" : 20
		}
usr = input ("Username: ")		#ASKS USER TO INPUT THEIR USERNAME
if  usr in logins:				#IF THEIR USERNAME EXISTS...
	pwd = input("Password: ")		#save var "pwd" as the user's input of a password
	encrypt = sha256(pwd.encode('utf-8')).hexdigest()	#encrypt their password so it will match to the dictionary's encrypted listing and set to var "encrypt".
	if logins[usr] == encrypt:	#IF THEIR USERNAME IS PAIRED WITH THE ENCRYPTED PWD...
		print("Welcome")		
	else:						#IF PWD IS INCORRECT...
		print("Incorrect password, Try again")
	
else:							#IF USERNAME DOES NOT EXIST, ASKS THEM TO CREATE NEW USERNAME AND PASSWORD.
	print("No such username...Create New")
	usrNew = input("Create Username:")	#saves var of new usrname
	logins[usrNew] = 10			#creates element in dictionary of new username.
	pwdNew = input("Create Password:")	#saves var of new pwd
	pwdCrypt = sha256(pwdNew.encode('utf-8')).hexdigest()
	logins[usrNew] = pwdCrypt
	usr = input("Username: ")	#Logs you in again
	pwd = input("Password: ")
	encrypt = sha256(pwd.encode('utf-8')).hexdigest()
	if logins[usr] == encrypt:		#checks if login has value of var "encrypt" which is the encrypted password.
		print("Welcome")
	else:
		errors = 0
		print("Incorrect password, Try again")
		if errors >= 4:
			print("Locked... Try again in 5 min")
			time.sleep(300)
			
		
	
	
