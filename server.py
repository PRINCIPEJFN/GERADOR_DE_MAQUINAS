# <warn> SHOULD NOT HAVE ANY FOLDERIN MEMOY PATH

import socket

import time as TL
#	server

import random as r

import os

PATH_GOODS_MEMORY = "/storage/emulated/0/GERADOR MAQUINA/memory/existis/"

PATH_LINKS = "/storage/emulated/0/GERADOR MAQUINA/memory/linked/"

PATH_CONTRIBUTIONS = "/storage/emulated/0/GERADOR MAQUINA/memory/contributions"

PATH_DICTIONARY = "/storage/emulated/0/GERADOR MAQUINA/dictionary.txt"

HOST = "127.0.0.117"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)



print("SERVER ", HOST, PORT)


path = PATH_GOODS_MEMORY



# SETTINGS

SETTING_LOGGIN = False

def save_new_file(name, content, IP):
	global path 
	#print("open")
	f = open(path+ name +".txt", "a")
	#print("wirte")
	f.write(str(content)[3:-1])
	#print("close")
	f.close()
	print("ADD UP:", content, "named as ", name, " BY", IP)

def save_option(inst, HOST):
	#print("save new file")
	save_new_file(str(r.randint(10000000,99999999)), inst, HOST)
	#print("saved instruction", inst)


def read_file(path):
	f = open(path, "r")
	
	return f.read()
	
def search_file(content):
	REAL = ""
	global GOODS_MEMORY_PATH
	arr = os.listdir(GOODS_MEMORY_PATH)
	for FP in arr:
		cont = read_file(GOODS_MEMORY_PATH +FP)
		#print("input", content)
		if str(content)[3:-1] == cont:
			REAL = FP
			print("found at number", FP)
			os.remove(GOODS_MEMORY_PATH + FP)
			print("removed",GOODS_MEMORY_PATH + FP )
	return REAL

def C_FILES():
	R = 0
	global GOODS_MEMORY_PATH
	
	arr = os.listdir(PATH_GOODS_MEMORY)
	
	for F in arr:
		R = R + 1
	
	
	if R > 10 and r.randint(0, 99999999) == 1:
		R = int(R - (R * .378)) 
	
	return R

def delete_instruction(inst):
	print("instruction deleted", inst) 
	
	search_file(inst)

def count_insertions():
	return 0

def WRITE_RESPONSE(arg0, arg1):
	global PATH_LINKS
	
	
	RT = r.randint(1000000, 99999999)
	os.mkdir(PATH_LINKS + str(RT))
	
	F = open(PATH_LINKS + str(RT)+ "/request.txt", "w")
	F.write(arg0)
	F.close()
	
	F1 = open(PATH_LINKS + str(RT) + "/response.txt", "w")
	F1.write(arg1)
	F1.close()
	

def SAVE_NEW_BEST(BEST, HOST, PORT):
	global PATH_CONTRIBUTIONS
	
	RN = r.randint(10000000, 99999999)
	F = open(PATH_CONTRIBUTIONS +"/" + str(RN) + ".txt" , "w")
	F.write(str(BEST)[2:-1]+ "::" + str(HOST) + "::"+ str(PORT))
	F.close()
	

def GET_DICTIONARY():
	global PATH_DICTIONARY
	F = open(PATH_DICTIONARY, "r")
	C = F.read()
	F.close()
	return C

def storage():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT))
	    s.listen()
	    conn, addr = s.accept()
	    with conn:
	        print(f"Connected by {addr}")
	        while data := conn.recv(1024):
	            #print("restart")
	            
	           # print("-:;")
	            if len(data) > 1 or data:
	            	#print(data)
	            	#print("prining", str(data)[2:len(data)-1])
	            #	print("recived ", data)
	            #	TL.sleep(12)()
	            
	            	if str(data)[2:len(data)].startswith("DEL "):
	            		delete_instruction(data[3:len(data)])
	            		conn.sendall(str("REMOVED  FROM MEMOY " + str(data[3:len(data)])[3:-1]).encode("utf8"))
	            	if str(data)[2:len(data)].startswith("INSERT "):
	            		save_option(data[6:len(data)], HOST)
	            		conn.sendall(str("ADD UP: " + str(data)[6:len(data)]).encode("utf8"))
	            	if (str(data))[2:-1].startswith("SD"):
	            		print("SDD MEMORY TOTAL USAGE")
	            		conn.sendall(str('MEMORY USAGE:  ' + str(C_FILES()) + " FILES").encode("utf8"))
	            	if (str(data)[2:-1].startswith("BEST ")):
	            		print("NEW BEST", data)
	            		SAVE_NEW_BEST(data, HOST, PORT)
	            	if (str(data)[2:-1] == "DOWNLOAD DICTIONARY"):
	            		conn.sendall(str(GET_DICTIONARY()).encode("utf8"))
	            	if (str(data)[2:-1]).startswith("ADD WORD"):
	            		F = open(PATH_DICTIONARY, "a")
	            		CUT = str(data)[2:-1]
	            		F.write("\n"+CUT[9:])
	            		F.close()
	            		conn.sendall(b'ADD NEW WORD COMPLETE')
	            	if (str(data)[2:-1]).startswith("INSERT_TABLE"):
	            		TEXT = str(str(data)[2:-1])[13:]
	            		ARG0 = TEXT.split("::")[0]
	            		ARG1 = TEXT.split("::")[1]
	            		print("INSERT TABLE", TEXT.split("::")[0], TEXT.split("::")[1])
	            		WRITE_RESPONSE(ARG0, ARG1)
	            		#conn.sendall("ADD UP: "+ data[2:len])
					
	            		#print("func insert")
	            #	print(data[3:len(data)])
	            #	TL.sleep(4)
	            #	print("af")
	            # 
	           
	            # print("RECV")
	            # conn.sendall(b'wo')
	            #   print("hhb")
	            #	print("recived", data)
	            #	print("end")
	            #if not data:
	            #     break
	            # else:
	            #    	print("else")
	            #     	storage()
	         	  
	            
# MACHINE GENERATOR
while True:
	storage()