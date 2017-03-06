import  socket


class Client_socket:

    def __init__(self,server_ip,ser_port):
        self.server_ip = server_ip
        self.ser_port = ser_port

    def  clientSocket_create(self):

        client_sokcet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_sokcet.connect((self.server_ip,self.ser_port))
        client_sokcet.send('hello world')
        data = client_sokcet.recv(1024)
        print "reply from server %s" %data


if __name__=="__main__":
    Client_socket('127.0.0.1',8023).clientSocket_create()
