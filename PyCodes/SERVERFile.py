import socket
import pickle
import numpy as np
import GmmVerification as GND
## Change the Host according to the port being communicated
host= '127.0.0.1'
port= 5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

pair=(host,port)

server.bind(pair)

server.listen(1)
	
while True:

	con,client=server.accept()
	print('Connection Established with : ',client)

	while True:

		message=con.recv(1024)
		A=message.decode('utf-8')
		if not message: break

		if A == 'Cad':

			IDMessage=con.recv(1024)
			
			IDRecv=IDMessage.decode('utf-8')

			File=open('IDS','rb')
			
			IDList=pickle.load(File)
			File.close()
			
			if IDRecv in IDList:
				IDMessage='ID already exists'
				con.send(IDMessage.encode('utf-8'))

			else: 
				NFile=open('IDS','wb')
				NList=IDList.append(IDRecv)
				pickle.dump(NList,NFile)

				IDCreated='ID Created' 
				con.send(IDCreated.encode('utf-8'))
		
				DirectoryAudio=con.recv(1024).decode('utf-8')
			
				GND.TrainModel(DirectoryAudio,IDRecv)

				MCreated='Model Created Succesfully'

				con.send(MCreated.encode('utf-8'))

		if A == 'Ver':

			data=con.recv(4096)
			ID,Audio= pickle.loads(data)

			Answer=GND.Verification(ID,Audio)

			con.send(Answer.encode('utf-8'))



	print("Connection Finished")
	con.close()

