import socket

host='127.0.0.1'
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

pair=(host,port)
client.connect(pair)

print('Conexao feita\n Digite 55 para sair')

message= raw_input()
while message!=55:

	client.send(message)

        message=raw_input()

client.close()

