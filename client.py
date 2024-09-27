import socket
import time
import threading

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

#  dispaly message from the server
def receive_msg_server(client):
    while True:
        try: 
            response = client.recv(1024).decode(FORMAT)
            if response: 
                print(f"Server: {response}")
        except Exception as e:
            print("ERROR!")
            client.close()
            break

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return

    connection = connect()
    # handle income message from server 
    receive_thread = threading.Thread(target = receive_msg_server, args=(connection,))
    receive_thread.start()
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()
