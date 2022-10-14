import socket
from decoder import decoder, encoder
import threading

HOST= '127.0.0.1'
PORT = 1234
NICKNAME =  input('chppse a nickname :\n')


client_socket = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname()  ,PORT)) 
 
def reciever():
    while True:
        try:
            message = decoder(client_socket.recv(1024))
            if message=='welcome':
                client_socket.send(encoder(NICKNAME))
            else:
                print(message)
        except:
            print('an errror occured!!')
            client_socket.close()
            break

def writer():
    while True: 
        msg = input()
        message = '{} :'.format(NICKNAME)+str(msg)
        client_socket.send(encoder(message))


t1 = threading.Thread(target=reciever)
t1.start()
t2 = threading.Thread(target=writer)
t2.start()

