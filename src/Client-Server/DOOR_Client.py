import socket
import pickle
##Change the host address and port according to the server
host='200.144.244.229'
port=2222

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

pair=(host,port)

client.connect(pair)

print("Type TERM to exit")

OPTIONS=input('Type -Cad to register a new model or -Ver to perform the Verification: ')
client.sendto(OPTIONS.encode('utf-8'),(host,port))

while (OPTIONS!='TERM') :

	
	if OPTIONS == 'Cad':
		ID=input('Type the ID to Register ')
		client.sendto(ID.encode('utf-8'),pair)
		Message=client.recv(1024).decode('utf-8')
		print(Message)
		
		if Message=='ID Created':

			Address=input('Train Audio Path on the Server :')
			client.sendto(Address.encode('utf-8'),pair)

			NMessage=client.recv(1024).decode('utf-8')

			print(NMessage)

	if OPTIONS == 'Ver':

		ID=input('ID: ')

		AudioIn=input('Audio for Verification: ')

		ToSend=pickle.dumps([ID,AudioIn])

		client.sendto(ToSend,pair)

		USER=client.recv(1024).decode('utf-8')

		print(USER)

	OPTIONS=input('Waiting: ')
	client.sendto(OPTIONS.encode('utf-8'),pair)

client.close()
