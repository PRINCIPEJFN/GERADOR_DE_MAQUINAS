import socket

import random as r

import os

LOCAL_MEMORY_PATH_GOOD = "/storage/emulated/0/GERADOR MAQUINA/local/memory/good"
LOCAL_MEMORY_PATH_BAD = "/storage/emulated/0/GERADOR MAQUINA/local/memory/bad"

LOCAL_DICTIONARY_PATH = "/storage/emulated/0/GERADOR MAQUINA/local/dictionary.txt"

HOST = "127.0.0.117"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

SAVE_ON_MEMORY = True
USE_LOCAL_DICTIONARY  = False
RANDOM_TEXT = True
EPOCHS = 347

print("CLIENT V1.0 ")

print("help - TYPE ON KEYBOARD INSERT sentence or DEL sentence OR FEW MORE COMMANDS  SSD TO SEE MEMORY USAGE INSERT_TABLE sent0::sent1 FOR CREATE TABLES CONNECTED TIPS FOR TEXT TIPS  xxyyinnzk xnv.....")

print("")
print("SET UP TO CONNECT TO ", HOST, PORT)




if False:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b"Hello, world")
		data = s.recv(1024)

data =""

m987 = False

def send_instruction(s, inst):
	global data
	global HOST
	global PORT
	global m987
	
	if m987 == False:
		print("connecting....")
		s.connect((HOST, PORT))
		m987 = True
		print("connected")
	if False:
		print("Not Conncted to Host Server not OnLine")
	#rint(s.status())
	s.sendall(inst.encode("utf8"))
	data = s.recv(1024)
	
print("")
print("starting..........")
for i in range(12):
	print("")

def RC():
	A = "abcdefghijklmoprqtuvwxyz "
	return A[r.randint(0, len(A)-1)]


def TIP():
	TR = ""
	for i in range(90):
		TR = TR + RC()
	return TR


def SAVE_GOOD(inst):
	global LOCAL_MEMORY_PATH_GOOD
	RT = r.randint(10000000, 99999999)
	F = open(LOCAL_MEMORY_PATH_GOOD+ "/" + str(RT)+ ".txt", "a")
	
	
	F.write(inst)
	
	F.close()
	return 1

def SAVE_BAD(inst):
	global LOCAL_MEMORY_PATH_BAD
	RT = r.randint(10000000, 99999999)
	F = open(LOCAL_MEMORY_PATH_BAD+ "/" + str(RT) + ".txt", "a")
	
	
	F.write(inst)
	
	F.close()
def COUNT_MEMORY():
	n = 0
	 
	return n

def RANDOM_WORD():
	global LOCAL_DICTIONARY_PATH
	
	F = open(LOCAL_DICTIONARY_PATH, "r")
	T = F.read()
	F.close()
	
	ARR = T.split("\n")
	return ARR[r.randint(0, len(ARR)-1)]

def generate_random():
	R = ""
	for I in range(12):
		R = R + RANDOM_WORD()
		
	return R

def read_file(path):
	CONTENT = ""
	F = open(path, "r")
	CONTENT = F.read()
	F.close()
	return CONTENT

def GOODS(TEXT):
	C = 0
	ARR = os.listdir(LOCAL_MEMORY_PATH_GOOD+"/")
	for F in ARR:
		PART = read_file(LOCAL_MEMORY_PATH_GOOD+"/"+F)
		if (PART in TEXT ):
			C = C + 1
	return C

def BAD(TEXT):
	C = 0
	ARR = os.listdir(LOCAL_MEMORY_PATH_BAD+"/")
	for F in ARR:
		PART = read_file(LOCAL_MEMORY_PATH_BAD+"/"+F)
		if (PART in TEXT ):
			C = C + 1
	return C


def calculate(TEXT):
	SUM = 0
	SUM = GOODS(TEXT) + 0
	SUM = SUM - BAD(TEXT)
	return SUM + 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	while True:
	
		a = input()
		
		if a == "TIP":
			print("TIP ", TIP())
		if a == "CONTRIBUTE":
			CM = COUNT_MEMORY()
			
			if USE_LOCAL_DICTIONARY == False:
				print("DOWNLOADING DICTIONARY")
				send_instruction(s, "DOWNLOAD DICTIONARY")
				print("DOWNLOAD COMPLETE")
				F = open(LOCAL_DICTIONARY_PATH, "w")
				F.write(str(data)[2:-1])
				F.close()
				print("DICTIONARY INSTALLED")
			BEST = 0
			solution = ""
			print("CALCULATING BEST")
			for I in range(EPOCHS):
				generated = generate_random()
				if calculate(generated) > BEST:
					solution = generated
					BEST = calculate(generate)
			print("COMPLETE", BEST,  generated)
			send_instruction(s, "BEST " + generated)
		else:
			send_instruction(s, a)
			if (SAVE_ON_MEMORY == True):
				if a.startswith("INSERT"):
					SAVE_GOOD(a[7:])
			if "MEMORY" in str(data):
				print(str(data))
			if "ADD UP" in str(data):
				print(str(data))
			if "REMOVED" in str(data):
				print(str(data))
			if "INSERTED" in str(data):
				print(str(data))
			else:
				1*1
			#print("sended")
		





#	print(f"STATUS: {data!r}")