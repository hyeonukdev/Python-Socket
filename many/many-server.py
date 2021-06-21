import socket, threading

host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


# 서버가 받은 메시지를 클라이언트 전체에 보내기
def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            # 클라이언트로부터 타당한 메시지를 받았는지 확인
            message = client.recv(1024)

            # 브로드캐스트 함수 동작
            broadcast(message)

        except:
            # 클라이언트가 나갔으면 알림
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left!\n".format(nickname).encode('ascii'))
            broadcast("{} people in this room!\n".format(len(nicknames)).encode('ascii'))
            nicknames.remove(nickname)
            break


# 멀티 클라이언트를 받는 메서드
def receive():
        while True:
            client, address = server.accept()
            print("Connected with {}".format(str(address)))
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)
            print("Nickname is {}".format(nickname))
            broadcast("{} joined!\n".format(nickname).encode('ascii'))
            broadcast("{} people in this room!\n".format(len(nicknames)).encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()


receive()