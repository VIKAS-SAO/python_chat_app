import socket
from decoder import decoder, encoder
import threading

HOST= '127.0.0.1'
PORT = 1234
from decoder import decoder , encoder



server_socket = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname()  ,PORT))
server_socket.listen(2)


 

CLIENT_ARRAY =[]
NICKNAMES_ARRAY=[]

def send_message(message ,client  ):
    for i in range(0,len(CLIENT_ARRAY)):
        if CLIENT_ARRAY[i]==client:
            continue
        CLIENT_ARRAY[i].send(encoder(message))



def listener(client ):
    while True:
        try:
            message = client.recv(1024)
            send_message(decoder(message) ,client )
        except:
            index = CLIENT_ARRAY.index(client)
            CLIENT_ARRAY.remove(client)
            client.close()
            nick = NICKNAMES_ARRAY[index]
            NICKNAMES_ARRAY.remove(nick)
            break


def acceptor():
    while True:
        client ,addr  = server_socket.accept()
        client.send(encoder('welcome'))
        nick = decoder(client.recv(1024))

        print('connected with {} at : '.format(nick) ,str(addr))
        
        send_message('{} joined the chat!'.format(nick) , None)
        NICKNAMES_ARRAY.append(nick)
        CLIENT_ARRAY.append(client)
        t = threading.Thread(target=listener ,args = [client])
        t.start()



acceptor()










 