import socket

host='127.0.0.1'
port=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

pair=(host,port)
client.connect(pair)

print('Conexao feita\n Digite TERM para sair')

message= raw_input()
while message!='TERM':

	client.send(message)

        message=raw_input()

client.close()

