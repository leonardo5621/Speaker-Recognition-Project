import socket
import pickle

host='127.0.0.1'
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

pair=(host,port)

client.connect(pair)

print("Digite 55 para sair")

whatUwannaDo=input('Digite -Cad Para Realizar Cadastro ou -Ver para fazer o Reconhecimento: ')
client.sendto(whatUwannaDo.encode('utf-8'),(host,port))

while (whatUwannaDo!='55') :

	
	if whatUwannaDo == 'Cad':
		ID=input('Digite o ID para Cadastrar ')
		client.sendto(ID.encode('utf-8'),pair)
		Message=client.recv(1024).decode('utf-8')
		print(Message)
		
		if Message=='ID Criado':

			Address=input('Coloque o endereco das amostras de treinamento :')
			client.sendto(Address.encode('utf-8'),pair)

			NMessage=client.recv(1024).decode('utf-8')

			print(NMessage)

	if whatUwannaDo == 'Ver':

		ID=input('Coloque seu ID: ')

		AudioIn=input('Audio para Verificacao: ')

		ToSend=pickle.dumps([ID,AudioIn])

		client.sendto(ToSend,pair)

		YouAre=client.recv(1024).decode('utf-8')

		print(YouAre)

	whatUwannaDo=input('Esperando Mensagem: ')
	client.sendto(whatUwannaDo.encode('utf-8'),pair)

client.close()
