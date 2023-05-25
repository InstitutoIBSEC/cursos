#server
import socket
import random

#abre conexao
c = socket.socket()
c.bind(('0.0.0.0',8081))
c.listen(50)
print("Servidor iniciado aguardando conexao")
c, addr = c.accept()
print('[+] Recebeu conexao de:', addr)

#escolhe a fruta
lines=open("lista.txt").read().splitlines()
fruta = random.choice(lines)
informacao=fruta

#envia resposta
c.send(str(informacao).encode())
print("mensagem enviada, fechando conexao")
c.close()